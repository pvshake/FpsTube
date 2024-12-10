import os
import json
import subprocess
from datetime import datetime

from kombu import Connection, Exchange


class VideoConverter:
    def __init__(self, rabbit_channel, db_conn, root_path):
        self.rabbit_channel = rabbit_channel
        self.db_conn = db_conn
        self.root_path = root_path

    def is_processed(self, video_id):
        with self.db_conn:
            cur = self.db_conn.cursor()
            cur.execute("""
                SELECT EXISTS(
                    SELECT 1 FROM processed_videos WHERE video_id = ? AND status = 'success'
                )
            """, (video_id,))
            return cur.fetchone()[0] == 1

    def mark_processed(self, video_id):
        with self.db_conn:
            cur = self.db_conn.cursor()
            cur.execute("""
                INSERT INTO processed_videos (video_id, status, processed_at)
                VALUES (?, ?, ?)
            """, (video_id, "success", datetime.now().isoformat()))

    def register_error(self, error_data):
        with self.db_conn:
            cur = self.db_conn.cursor()
            cur.execute("""
                INSERT INTO process_errors_log (error_details, created_at)
                VALUES (?, ?)
            """, (json.dumps(error_data), datetime.now().isoformat()))

    def handle_message(self, task, conversion_exch, confirmation_key, conn: Connection):
        video_id = task.get("video_id")
        path = task.get("path")

        if self.is_processed(video_id):
            print(f"Video {video_id} already processed")
            return

        try:
            self.process_video(video_id, path)
            self.mark_processed(video_id)

            exchange = Exchange(conversion_exch, type='direct', auto_delete=False)
            exchange.declare(channel=conn.channel())

            producer = conn.Producer(serializer='json')
            producer.publish(
                {"video_id": video_id, "path": path},
                exchange=conversion_exch,
                routing_key=confirmation_key
            )
            print(f"Published confirmation message for video {video_id}")
        except Exception as e:
            error_data = {
                "video_id": video_id,
                "error": str(e),
                "time": datetime.now().isoformat()
            }
            self.register_error(error_data)

    def process_video(self, video_id, path):
        chunk_path = os.path.join(self.root_path, str(video_id))
        merged_file = os.path.join(chunk_path, "merged.mp4")
        mpeg_dash_path = os.path.join(chunk_path, "mpeg-dash")

        self.merge_chunks(chunk_path, merged_file)

        os.makedirs(mpeg_dash_path, exist_ok=True)

        ffmpeg_cmd = [
            "ffmpeg", "-i", merged_file,
            "-f", "dash",
            os.path.join(mpeg_dash_path, "output.mpd")
        ]
        subprocess.run(ffmpeg_cmd, check=True)
        os.remove(merged_file)

    def merge_chunks(self, input_dir, output_file):
        chunks = sorted(
            [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".chunk")],
            key=lambda x: int("".join(filter(str.isdigit, os.path.basename(x))))
        )

        with open(output_file, "wb") as merged:
            for chunk in chunks:
                with open(chunk, "rb") as f:
                    merged.write(f.read())
