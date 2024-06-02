import tkinter as tk
import tkinter.ttk as ttk

import plot_stuff as ps

def window(plot_buttons):
    root = tk.Tk()
    root.title('Hotel Booking Analysis')

    # Styling
    bg_color = "#151515" # Dark grey
    button_color = "#A91D3A" # Dark red
    button_fg_color = "#EEEEEE" # Light grey
    font_family = "Monospace"
    font_size = 13

    # Configure root window styles
    root.configure(bg=bg_color)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E))

    # Button style
    style = ttk.Style()
    style.configure("TButton",
        background=button_color,
        foreground=button_fg_color,
        borderwidth=3,
        font=(font_family, font_size)
    )

    # Hover style
    style.map("TButton",
        background=[("active", "#C73659")],
        foreground=[("active", button_fg_color)]
    )

    # Create buttons
    for i, (text, command) in enumerate(plot_buttons.items()):
        # Wrap the command in a lambda to call show_plot after the plotting function
        btn_command = lambda cmd=command: (cmd(), ps.show_plot(), print("--------------"))
        ttk.Button(button_frame, text=text, command=btn_command).grid(row=i, column=0, sticky=(tk.W, tk.E))
    
    # Close button to exit the application
    close_button = ttk.Button(root, text="Close", command=root.quit)
    close_button.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))

    root.mainloop()