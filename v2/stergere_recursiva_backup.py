import os
import time
import logging
import datetime
import argparse

def delete_old_files(directory, days_to_delete, excluded_months):
    current_time = time.time()
    execution_date = datetime.datetime.now()

    logging.basicConfig(format='%(message)s', filename='AutoDelete.log', level=logging.INFO)
    logger = logging.getLogger()

    for dirpath, _, filenames in os.walk(directory):
        dirname = os.path.basename(dirpath)
        print(f'--- {dirname} ---')

        for filename in filenames:
            file_path = os.path.abspath(os.path.join(dirpath, filename))
            modified_time = os.path.getmtime(file_path)
            file_month = int(time.strftime('%m', time.localtime(modified_time)))

            print(f'File month: {file_month}')
            print(f'File: {file_path}')

            if file_month not in excluded_months:
                if (current_time - modified_time) // (24 * 3600) >= days_to_delete:
                    os.unlink(file_path)
                    print(f'{file_path} has been deleted.\n')
                else:
                    print(f'{file_path} was not deleted.')
            else:
                print(f'{file_path} was not deleted (excluded month).')

    print('--- EXECUTION COMPLETE ---')
    print(execution_date)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete old backup files except those from certain months.")
    parser.add_argument("--directory", required=True, help="Target directory to clean")
    parser.add_argument("--days", type=int, required=True, help="Minimum file age in days before deletion")
    parser.add_argument("--exclude-months", nargs=2, type=int, metavar=('MONTH1', 'MONTH2'),
                        help="Two months to exclude from deletion (e.g., 12 1)")

    args = parser.parse_args()
    delete_old_files(args.directory, args.days, set(args.exclude_months))
