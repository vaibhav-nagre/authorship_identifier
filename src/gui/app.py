import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from core.authorship_identifier import process_data, extract_author_name

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSIC 691 - Authorship Identifier")
        self.root.geometry("800x600")

        # Create a menu bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Add file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.select_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Add help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        # frame for the file selection and analysis
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Select a file for authorship analysis:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.select_button = tk.Button(self.frame, text="Select File", command=self.select_file)
        self.select_button.grid(row=0, column=1, padx=10, pady=10)

        # text area to display the file content
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(pady=10)

        # label to display the result
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.display_file_content(file_path)
            self.analyze_file(file_path)

    def display_file_content(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.INSERT, content)

    def analyze_file(self, file_path):
        known_dir = 'known_authors'
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File '{file_path}' not found.")
            return

        best_match_file = process_data(file_path, known_dir)
        print(f"Debug: best_match_file = {best_match_file}")  # Debug print
        author_name = extract_author_name(best_match_file)
        print(f"Debug: author_name = {author_name}")  # Debug print
        self.result_label.config(text=f"The most likely author match for '{file_path}' is: {author_name}")

    def show_about(self):
        messagebox.showinfo("About", "Authorship Identifier v1.0\nDeveloped by Your Name")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()