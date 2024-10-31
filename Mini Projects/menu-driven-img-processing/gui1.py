import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps
import os
import time
import numpy as np

# List of input files from the 'input' directory
input_dir = './input'
inputFiles = [f for f in os.listdir(input_dir) if f.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif','webp'))]

# Function to load an image
def load_image(file_path):
    image = Image.open(file_path)
    return image

def update_image_display(image):
    """Display the image in the GUI after modifications."""
    img = ImageTk.PhotoImage(image)
    img_label.config(image=img)
    img_label.image = img  # Keep a reference to avoid garbage collection

def image_operations():
    """Open the Image Operations interface."""
    if not inputFiles:
        messagebox.showinfo("No Images Found", "No images found in the input directory.")
        return

    # Create a new window for image operations
    img_ops_window = tk.Toplevel(root)
    img_ops_window.title("Image Operations")
    img_ops_window.geometry("600x500")

    selected_image = tk.StringVar(value=inputFiles[0])

    # Drop-down menu to select an image
    ttk.Label(img_ops_window, text="Select an Image:").grid(row=0, column=0, padx=5, pady=5)
    img_dropdown = ttk.Combobox(img_ops_window, textvariable=selected_image, values=inputFiles)
    img_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Load and display the selected image
    def load_selected_image():
        file_name = selected_image.get()
        file_path = os.path.join(input_dir, file_name)
        global current_image, preview_image
        current_image = load_image(file_path)
        preview_image = current_image.copy()  # Use a copy for preview
        update_image_display(preview_image)

    ttk.Button(img_ops_window, text="Load Image", command=load_selected_image).grid(row=0, column=2, padx=5, pady=5)

    # Operations Frame
    operations_frame = ttk.LabelFrame(img_ops_window, text="Operations")
    operations_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")

    # Resize
    def preview_resize():
        width = int(width_entry.get())
        height = int(height_entry.get())
        resized_img = preview_image.resize((width, height))
        update_image_display(resized_img)

    def apply_resize():
        global current_image
        width = int(width_entry.get())
        height = int(height_entry.get())
        current_image = current_image.resize((width, height))
        update_image_display(current_image)

    ttk.Label(operations_frame, text="Resize to (WxH):").grid(row=0, column=0, padx=5, pady=5)
    width_entry = ttk.Entry(operations_frame, width=5)
    width_entry.grid(row=0, column=1)
    height_entry = ttk.Entry(operations_frame, width=5)
    height_entry.grid(row=0, column=2)
    ttk.Button(operations_frame, text="Preview Resize", command=preview_resize).grid(row=0, column=3, padx=5)
    ttk.Button(operations_frame, text="Apply Resize", command=apply_resize).grid(row=0, column=4, padx=5)

    # Rotate
    def preview_rotate():
        angle = int(angle_entry.get())
        rotated_img = preview_image.rotate(angle)
        update_image_display(rotated_img)

    def apply_rotate():
        global current_image
        angle = int(angle_entry.get())
        current_image = current_image.rotate(angle)
        update_image_display(current_image)

    ttk.Label(operations_frame, text="Rotate by:").grid(row=1, column=0, padx=5, pady=5)
    angle_entry = ttk.Entry(operations_frame, width=5)
    angle_entry.grid(row=1, column=1)
    ttk.Button(operations_frame, text="Preview Rotate", command=preview_rotate).grid(row=1, column=3, padx=5)
    ttk.Button(operations_frame, text="Apply Rotate", command=apply_rotate).grid(row=1, column=4, padx=5)

    # Flip
    def preview_flip(direction):
        if direction == "Horizontal":
            flipped_img = preview_image.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == "Vertical":
            flipped_img = preview_image.transpose(Image.FLIP_TOP_BOTTOM)
        update_image_display(flipped_img)

    def apply_flip(direction):
        global current_image
        if direction == "Horizontal":
            current_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == "Vertical":
            current_image = current_image.transpose(Image.FLIP_TOP_BOTTOM)
        update_image_display(current_image)

    ttk.Label(operations_frame, text="Flip:").grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(operations_frame, text="Preview Horizontal", command=lambda: preview_flip("Horizontal")).grid(row=2, column=1)
    ttk.Button(operations_frame, text="Preview Vertical", command=lambda: preview_flip("Vertical")).grid(row=2, column=2)
    ttk.Button(operations_frame, text="Apply Horizontal", command=lambda: apply_flip("Horizontal")).grid(row=2, column=3)
    ttk.Button(operations_frame, text="Apply Vertical", command=lambda: apply_flip("Vertical")).grid(row=2, column=4)

    # Save
    def save_image():
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            current_image.save(file_path)
            messagebox.showinfo("Image Saved", f"Image saved to {file_path}")

    ttk.Button(img_ops_window, text="Save Image", command=save_image).grid(row=3, column=1, pady=10)

    # Label for displaying images
    global img_label
    img_label = ttk.Label(img_ops_window)
    img_label.grid(row=4, column=0, columnspan=3, pady=10)

    # Load the initially selected image
    load_selected_image()

def image_processing():
    """Open the Image Processing interface."""
    if not inputFiles:
        messagebox.showinfo("No Images Found", "No images found in the input directory.")
        return

    # Create a new window for image processing
    img_proc_window = tk.Toplevel(root)
    img_proc_window.title("Image Processing")
    img_proc_window.geometry("600x500")

    selected_image = tk.StringVar(value=inputFiles[0])

    # Drop-down menu to select an image
    ttk.Label(img_proc_window, text="Select an Image:").grid(row=0, column=0, padx=5, pady=5)
    img_dropdown = ttk.Combobox(img_proc_window, textvariable=selected_image, values=inputFiles)
    img_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Load and display the selected image
    def load_selected_image():
        file_name = selected_image.get()
        file_path = os.path.join(input_dir, file_name)
        global current_image, preview_image
        current_image = load_image(file_path)
        preview_image = current_image.copy()  # Use a copy for preview
        update_image_display(preview_image)

    ttk.Button(img_proc_window, text="Load Image", command=load_selected_image).grid(row=0, column=2, padx=5, pady=5)

    # Processing Frame
    processing_frame = ttk.LabelFrame(img_proc_window, text="Processing Options")
    processing_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")

    # Convert to Grayscale
    def preview_grayscale():
        grayscale_img = ImageOps.grayscale(preview_image)
        update_image_display(grayscale_img)

    def apply_grayscale():
        global current_image
        current_image = ImageOps.grayscale(current_image)
        update_image_display(current_image)

    ttk.Button(processing_frame, text="Preview Grayscale", command=preview_grayscale).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(processing_frame, text="Apply Grayscale", command=apply_grayscale).grid(row=0, column=1, padx=5, pady=5)

    # Convert to HSV
    def preview_hsv():
        hsv_img = preview_image.convert("HSV")
        update_image_display(hsv_img)

    def apply_hsv():
        global current_image
        current_image = current_image.convert("HSV")
        update_image_display(current_image)

    ttk.Button(processing_frame, text="Preview HSV", command=preview_hsv).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(processing_frame, text="Apply HSV", command=apply_hsv).grid(row=1, column=1, padx=5, pady=5)

    # Apply Blur
    def preview_blur():
        blurred_img = preview_image.filter(ImageFilter.BLUR)
        update_image_display(blurred_img)

    def apply_blur():
        global current_image
        current_image = current_image.filter(ImageFilter.BLUR)
        update_image_display(current_image)

    ttk.Button(processing_frame, text="Preview Blur", command=preview_blur).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(processing_frame, text="Apply Blur", command=apply_blur).grid(row=2, column=1, padx=5, pady=5)

    # Separate RGB Channels
    def preview_rgb_channels():
        """Preview of RGB channels by opening a temporary window to show channels."""
        r, g, b = preview_image.split()
        display_rgb_channels(r, g, b)

    def apply_rgb_channels():
        """Apply and display RGB channels by splitting the current_image."""
        r, g, b = current_image.split()
        display_rgb_channels(r, g, b)

    def display_rgb_channels(r, g, b):
        """Helper function to display RGB channels in a new window."""
        # Create a new window to display each channel
        channel_window = tk.Toplevel(img_proc_window)
        channel_window.title("RGB Channels")

        # Display each channel separately
        r_img = ImageTk.PhotoImage(r)
        g_img = ImageTk.PhotoImage(g)
        b_img = ImageTk.PhotoImage(b)

        tk.Label(channel_window, text="Red Channel").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(channel_window, image=r_img).grid(row=1, column=0, padx=5, pady=5)
        time.sleep(0.25)
        tk.Label(channel_window, text="Green Channel").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(channel_window, image=g_img).grid(row=1, column=1, padx=5, pady=5)
        time.sleep(0.25)
        tk.Label(channel_window, text="Blue Channel").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(channel_window, image=b_img).grid(row=1, column=2, padx=5, pady=5)

        # Keep a reference to avoid garbage collection
        channel_window.r_img = r_img
        channel_window.g_img = g_img
        channel_window.b_img = b_img

    ttk.Button(processing_frame, text="Preview RGB Channels", command=preview_rgb_channels).grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(processing_frame, text="Apply RGB Channels", command=apply_rgb_channels).grid(row=3, column=1, padx=5, pady=5)

    # Save
    def save_image():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            current_image.save(file_path)
            messagebox.showinfo("Image Saved", f"Image saved to {file_path}")

    ttk.Button(processing_frame, text="Save Image", command=save_image).grid(row=3, column=2, pady=10)

    # Label for displaying images
    global img_label
    img_label = ttk.Label(img_proc_window)
    img_label.grid(row=4, column=0, columnspan=3, pady=10)

    # Load the initially selected image
    load_selected_image()

def colour_detection():
    """Open the Colour Detection interface."""
    if not inputFiles:
        messagebox.showinfo("No Images Found", "No images found in the input directory.")
        return

    # Create a new window for color detection
    color_det_window = tk.Toplevel(root)
    color_det_window.title("Colour Detection")
    color_det_window.geometry("600x500")

    selected_image = tk.StringVar(value=inputFiles[0])

    # Drop-down menu to select an image
    ttk.Label(color_det_window, text="Select an Image:").grid(row=0, column=0, padx=5, pady=5)
    img_dropdown = ttk.Combobox(color_det_window, textvariable=selected_image, values=inputFiles)
    img_dropdown.grid(row=0, column=1, padx=5, pady=5)

    # Load and display the selected image
    def load_selected_image():
        file_name = selected_image.get()
        file_path = os.path.join(input_dir, file_name)
        global current_image
        current_image = load_image(file_path)
        update_image_display(current_image)

    ttk.Button(color_det_window, text="Load Image", command=load_selected_image).grid(row=0, column=2, padx=5, pady=5)

    # Target color inputs
    ttk.Label(color_det_window, text="Target Color (RGB):").grid(row=1, column=0, padx=5, pady=5)
    r_value = tk.IntVar(value=255)
    g_value = tk.IntVar(value=0)
    b_value = tk.IntVar(value=0)
    tk.Entry(color_det_window, textvariable=r_value, width=5).grid(row=1, column=1)
    tk.Entry(color_det_window, textvariable=g_value, width=5).grid(row=1, column=2)
    tk.Entry(color_det_window, textvariable=b_value, width=5).grid(row=1, column=3)

    # Tolerance input
    ttk.Label(color_det_window, text="Tolerance:").grid(row=2, column=0, padx=5, pady=5)
    tolerance_value = tk.IntVar(value=30)
    tk.Entry(color_det_window, textvariable=tolerance_value, width=5).grid(row=2, column=1)

    # Detect and highlight color function
    def detect_and_highlight():
        target_rgb = (r_value.get(), g_value.get(), b_value.get())
        tolerance = tolerance_value.get()

        # Convert image to numpy array for pixel-wise operations
        image_np = np.array(current_image.convert('RGB'))
        
        # Create a mask based on the tolerance level for the target color
        mask = ((abs(image_np[:, :, 0] - target_rgb[0]) <= tolerance) &
                (abs(image_np[:, :, 1] - target_rgb[1]) <= tolerance) &
                (abs(image_np[:, :, 2] - target_rgb[2]) <= tolerance))

        # Highlight target color areas by keeping them and dimming others
        highlighted_np = np.zeros_like(image_np)
        highlighted_np[mask] = image_np[mask]
        dimming_factor = 0.3  # Factor to dim non-matching pixels
        highlighted_np[~mask] = (image_np[~mask] * dimming_factor).astype(np.uint8)

        # Convert back to PIL Image and display
        highlighted_image = Image.fromarray(highlighted_np)
        update_image_display(highlighted_image)

    ttk.Button(color_det_window, text="Detect and Highlight Color", command=detect_and_highlight).grid(row=3, column=0, columnspan=4, padx=5, pady=10)

    # Label for displaying images
    global img_label
    img_label = ttk.Label(color_det_window)
    img_label.grid(row=4, column=0, columnspan=4, pady=10)

    # Load the initially selected image
    load_selected_image()


# Create the main window
root = tk.Tk()
root.title("GUI Interface")

# Create a frame for the buttons
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create buttons
btn_image_operations = ttk.Button(frame, text="Image Operations", command=image_operations)
btn_image_operations.grid(row=0, column=0, padx=5, pady=5)

btn_image_processing = ttk.Button(frame, text="Image Processing", command=image_processing)
btn_image_processing.grid(row=1, column=0, padx=5, pady=5)

btn_colour_detection = ttk.Button(frame, text="Colour Detection", command=colour_detection)
btn_colour_detection.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()

