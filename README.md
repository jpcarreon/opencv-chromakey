# Usage
## Dependencies
`pip install opencv numpy`

## Steps
1. Video with green screen should be named `main.mp4`
2. Frames the video will be chroma-keyed on should be placed inside a folder named `./frames/` and end with `.jpeg`
3. Use `python checkHSV.py` to record the proper lower and upper HSV of `main.mp4`
4. Set the recorded lower and upper HSV values on lines 17-18 of `main.py`
5. Ensure `finalOutput` on line 13 is set to 1
6. Run `python main.py`
7. Chroma-keyed frames will be saved on `./output/`