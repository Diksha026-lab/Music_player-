import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Global variables
playlist = []  # Stores the list of songs in the playlist
current_song_index = -1  # Tracks the current song being played
paused = False  # Tracks if the song is paused

# Function to load MP3 files and add to the playlist
def add_songs():
    songs = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    for song in songs:
        playlist.append(song)
        playlist_box.insert(tk.END, os.path.basename(song))

# Function to remove selected song from playlist
def remove_song():
    selected_song = playlist_box.curselection()
    if selected_song:
        playlist.pop(selected_song[0])
        playlist_box.delete(selected_song)

# Function to play the selected song 
def play_song():
    global current_song_index, paused
    if playlist_box.curselection():
        current_song_index = playlist_box.curselection()[0]
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        status.set(f"Playing: {os.path.basename(playlist[current_song_index])}")
        paused = False
    else:
        messagebox.showwarning("No Selection", "Please select a song to play.")

# Function to pause/resume the current song
def pause_resume_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        status.set(f"Resumed: {os.path.basename(playlist[current_song_index])}")
    else:
        pygame.mixer.music.pause()
        paused = True
        status.set("Paused")

# Function to stop the current song
def stop_song():
    pygame.mixer.music.stop()
    status.set("Stopped")

# Function to play the next song
def next_song():
    global current_song_index, paused
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        status.set(f"Playing: {os.path.basename(playlist[current_song_index])}")
        paused = False
    else:
        messagebox.showinfo("End of Playlist", "You have reached the end of the playlist.")

# Function to play the previous song
def previous_song():
    global current_song_index, paused
    if current_song_index > 0:
        current_song_index -= 1
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        status.set(f"Playing: {os.path.basename(playlist[current_song_index])}")
        paused = False
    else:
        messagebox.showinfo("Start of Playlist", "You are at the beginning of the playlist.")

# Create the root window
root = tk.Tk()
root.title("MP3 Player and Playlist Manager")
root.geometry("500x400")
root.configure(bg='lightblue')  # Set window background color

# Playlist box to display added songs
playlist_box = Listbox(root, selectmode=tk.SINGLE, width=50, height=12, bg='white', fg='black')
playlist_box.pack(pady=20)

# Status label
status = tk.StringVar()
status.set("No song playing")
status_label = tk.Label(root, textvariable=status, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10), bg='lightgray')
status_label.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

# Buttons for playlist management and playback controls
control_frame = tk.Frame(root, bg='lightblue')
control_frame.pack(pady=10)

add_button = tk.Button(control_frame, text="Add Songs", command=add_songs, bg='green', fg='white',width=15,height=2)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(control_frame, text="Remove Song", command=remove_song, bg='red', fg='white',width=15,height=2)
remove_button.grid(row=0, column=1, padx=10)

play_button = tk.Button(control_frame, text="Play", command=play_song, bg='blue', fg='white',width=15,height=2)
play_button.grid(row=1, column=0, padx=10)

pause_button = tk.Button(control_frame, text="Pause/Resume", command=pause_resume_song, bg='yellow', fg='black',width=15,height=2)
pause_button.grid(row=1, column=1, padx=10)

stop_button = tk.Button(control_frame, text="Stop", command=stop_song, bg='orange', fg='black',width=15,height=2)
stop_button.grid(row=2, column=0, padx=10)

previous_button = tk.Button(control_frame, text="Previous", command=previous_song, bg='purple', fg='white',width=15,height=2)
previous_button.grid(row=2, column=1, padx=10)

next_button = tk.Button(control_frame, text="Next", command=next_song, bg='pink', fg='black',width=15,height=2)
next_button.grid(row=2, column=2, padx=10)

# Main loop
root.mainloop()