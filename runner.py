import subprocess
import time

# Define the function to start the Flask application
def start_flask_app():
    # Replace 'app.py' with the filename of the Flask application
    subprocess.run(["python", "app.py"])

# Run the Flask application in a never-ending loop
while True:
    try:
        # Start the Flask application in a separate process
        process = subprocess.Popen(["python", "app.py"])

        # Wait for 3 minutes (180 seconds)
        time.sleep(30)

        # Terminate the Flask application process after 3 minutes
        process.terminate()
        process.wait()

    except KeyboardInterrupt:
        # Exit the loop if the user presses Ctrl+C
        break
