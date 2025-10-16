#!/home/dipesh-thakur/Documents/python_projects/venv/bin/python
import zipfile
import os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist!")
        return
    
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory!")
        return
    
    number = 1
    parent_dir = os.path.dirname(folder)
    base_name = os.path.basename(folder)
    
    while True:
        zipFilename = os.path.join(parent_dir, base_name + '_' + str(number) + '.zip')
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    
    print(f'Creating {zipFilename}....')
    
    with zipfile.ZipFile(zipFilename, 'w', zipfile.ZIP_DEFLATED) as backupZip:
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')
            
            # Calculate relative path for the folder
            relative_folder = os.path.relpath(foldername, folder)
            if relative_folder == '.': # only has files
                relative_folder = base_name
            else:
                relative_folder = os.path.join(base_name, relative_folder)
            
            backupZip.write(foldername, arcname=relative_folder)
            
            for filename in filenames:
                if filename.startswith(base_name + '_') and filename.endswith('.zip'):
                    continue
                
                # Full path to read the file
                file_path = os.path.join(foldername, filename)
                
                # Relative path for storage in ZIP
                archive_path = os.path.join(relative_folder, filename)
                
                backupZip.write(file_path, arcname=archive_path)
    
    print('Done.')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: ./backup.py <folder_path>")
        sys.exit(1)
    folder_to_backup = sys.argv[1]
    backupToZip(folder_to_backup)