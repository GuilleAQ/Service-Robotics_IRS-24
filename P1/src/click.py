import cv2
import matplotlib.pyplot as plt

# Click counter
click_count = 0

# Function to handle click events on the image
def on_click(event):
    global click_count
    # Check if the click is with the left mouse button
    if event.button == 1:
        # Increment the click counter
        click_count += 1
        
        # Get the coordinates (x, y) of the click
        x, y = int(event.xdata), int(event.ydata)
        print(f"Click #{click_count} - Coordinates: x={x}, y={y}")
        
        # Draw a circle at the click coordinates
        ax.plot(x, y, 'ro')  # 'ro' means a red point ('r' is red color, 'o' is for drawing a circle)

        # Display the text "click nº X" next to the click
        ax.text(x + 10, y, f"click nº {click_count}", color='red', fontsize=12)

        # Update the image to show the marker and text
        fig.canvas.draw()

# Load the image using OpenCV
try:
    img = cv2.imread("../resources/figures/mapgrannyannie.png")  # Make sure to set the correct image path

    # Check the dimensions of the image
    if img.shape[0] == 1012 and img.shape[1] == 1013:
        # Convert from BGR (OpenCV format) to RGB (matplotlib format)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Display the image using matplotlib
        fig, ax = plt.subplots()
        ax.imshow(img_rgb)

        # Connect the click event to the on_click function
        cid = fig.canvas.mpl_connect('button_press_event', on_click)

        print("Press CTRL+C to interrupt the program.")

        # Display the interactive window
        plt.show()

    else:
        print("The image does not have the dimensions of 1012x1013 pixels.")

except KeyboardInterrupt:
    print("\nInterruption detected. Closing the program.")
    plt.close('all')  # Close any open matplotlib windows
