import time
import tkinter as tk

def display_scene(scene, text_widget, callback=None):
    def afficher_paragraphes(index_paragraph=0, index_lettre=0):
        if index_paragraph < len(scene):
            paragraph = scene[index_paragraph]
            if index_lettre < len(paragraph):
                text_widget.config(state=tk.NORMAL)
                text_widget.insert(tk.END, paragraph[index_lettre])
                text_widget.see(tk.END)
                text_widget.update()
                text_widget.config(state=tk.DISABLED)
                text_widget.after(30, afficher_paragraphes, index_paragraph, index_lettre + 1)
            else:
                text_widget.config(state=tk.NORMAL)
                text_widget.insert(tk.END, '\n')
                text_widget.config(state=tk.DISABLED)
                text_widget.after(500, afficher_paragraphes, index_paragraph + 1, 0)
        else:
            if callback:
                callback()

    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.config(state=tk.DISABLED)
    afficher_paragraphes()

def display_choix(choix_list, rep_list, text_widget, button_frame, callback):
    # Efface les anciens boutons
    for widget in button_frame.winfo_children():
        widget.destroy()

    text_widget.config(state=tk.NORMAL)
    for i, choix in enumerate(choix_list):
        text_widget.insert(tk.END, f"{i+1}. {choix}\n")
    text_widget.config(state=tk.DISABLED)

    def on_choix(idx):
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, f"\n{rep_list[idx]}\n\n")
        text_widget.config(state=tk.DISABLED)
        for widget in button_frame.winfo_children():
            widget.config(state=tk.DISABLED)
        if callback:
            text_widget.after(1000, callback)

    for i, choix in enumerate(choix_list):
        btn = tk.Button(button_frame, text=choix, font=("Arial", 12), command=lambda idx=i: on_choix(idx))
        btn.pack(side=tk.LEFT, padx=5, pady=5)