# main.py
from modules.data_io import load_data, clean_data, export_to_csv
from modules.filtering import filter_data
from modules.summarization import display_summary, group_by_region, group_by_date
from modules.visualization import plot_time_trend
from modules.database import init_db, save_to_db, read_from_db

def main():
    file_path = "data/COVID-19_Vaccination_Rates.csv"
    df = None
    conn = init_db()

    while True:
        print("\n--- Public Health Dashboard ---")
        print("1. Load data")
        print("2. Clean data")
        print("3. Filter data")
        print("4. Display summary")
        print("5. Plot time trend")
        print("6. Group by region")
        print("7. Group by date")
        print("8. Export CSV")
        print("9. Save to DB")
        print("10. Read from DB")
        print("11. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            df = load_data(file_path)
            print(df.head() if df is not None else "Failed to load data")
        elif choice == '2':
            if df is not None:
                df = clean_data(df)
                print("Data cleaned")
            else:
                print("Load data first")
        elif choice == '3':
            if df is not None:
                region = input("Region: ").strip() or None
                stat = input("Statistic Label: ").strip() or None
                age = input("Age Group: ").strip() or None
                filtered_df = filter_data(df, region, stat, age)
                print(filtered_df.head())
            else:
                print("Load data first")
        elif choice == '4':
            if df is not None:
                print(display_summary(df))
            else:
                print("Load data first")
        elif choice == '5':
            if df is not None:
                region = input("Region: ").strip() or None
                stat = input("Statistic Label: ").strip() or None
                age = input("Age Group: ").strip() or None
                plot_time_trend(df, region, stat, age)
            else:
                print("Load data first")
        elif choice == '6':
            if df is not None:
                print(group_by_region(df))
            else:
                print("Load data first")
        elif choice == '7':
            if df is not None:
                print(group_by_date(df))
            else:
                print("Load data first")
        elif choice == '8':
            if df is not None:
                fname = input("CSV file name: ").strip()
                export_to_csv(df, fname)
            else:
                print("Load data first")
        elif choice == '9':
            if df is not None:
                save_to_db(df, conn)
            else:
                print("Load data first")
        elif choice == '10':
            print(read_from_db(conn))
        elif choice == '11':
            conn.close()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
