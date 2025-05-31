import pandas as pd


def to_dataframe(data):
    fnames = [f.rsplit("/")[-1] for f in data.metadata["video_paths"]]
    num_frames = [len(pts) for pts in data.metadata["video_pts"]]
    fps = [i for i in data.metadata["video_fps"]]
    subclips = [len(x) for x in data.video_clips.clips]
    metadata = pd.DataFrame(
        list(zip(fnames, num_frames, fps, subclips)),
        columns=["filepath", "frames", "fps", "clips"],
    )
    print(f"Length: {len(data)}")
    return metadata
