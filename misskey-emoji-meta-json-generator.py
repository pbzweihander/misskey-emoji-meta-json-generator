import os
import json


def main(root_path: str, category: str | None):
    output = {
        "emojis": [
            {
                "downloaded": True,
                "fileName": filename,
                "emoji": {
                    "name": filename.rsplit(".", 1)[0],
                    "category": category,
                    "aliases": [],
                },
            }
            for filename in os.listdir(root_path)
            if filename != "meta.json"
        ]
    }
    print(json.dumps(output))


if __name__ == "__main__":
    import sys

    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
