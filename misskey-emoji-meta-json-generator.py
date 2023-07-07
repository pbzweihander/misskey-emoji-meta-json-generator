import os
import json


def main(root_path: str):
    output = {
        "emojis": [
            {
                "downloaded": True,
                "fileName": filename,
                "emoji": {
                    "name": filename.rsplit(".", 1)[0],
                    "category": None,
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

    main(sys.argv[1])
