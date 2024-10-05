import concurrent.futures
import subprocess
import os

def run_script(script_path):
    subprocess.run(['python', script_path])

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_1 = os.path.join(base_dir, 'morgana-bot', 'main.py')
    script_2 = os.path.join(base_dir, 'stickerinator', 'main.py')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(run_script, script) for script in [script_1, script_2]]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Script finished with result: {result}")
            except Exception as e:
                print(f"Script generated an exception: {e}")
