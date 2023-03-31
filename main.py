import moviepy.editor as mp

# set the input file name
input_file = "input.gif"

# set the output file name
output_file = "output.mp4"

try:
    # read the gif file
    clip = mp.VideoFileClip(input_file)

    # convert the gif file to mp4
    clip.write_videofile(output_file)

    # print success message
    print("Conversion done")

except Exception as e:
    # print error message
    print("Conversion failed, try again")
