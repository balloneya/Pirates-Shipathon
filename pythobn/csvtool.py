#!/usr/bin/env python3
from pathlib import Path
import csv
import statistics
import sys
from typing import List, Tuple, Optional
import traceback


def copy_file(source_file: str, destination_file: Optional[str] = None) -> str:
    """
    Copy a CSV file from source to destination.

    Input:
        source_file (str): Path to source CSV file
        destination_file (Optional[str]): Path to destination file, auto-generated if None

    Output:
        str: Success message with destination filename, or error message

    Examples:
        copy_file('students.csv', 'backup.csv') -> "File copied successfully as backup.csv"
        copy_file('students.csv') -> "File copied successfully as students_copy.csv"
        copy_file('nonexistent.csv') -> "Error: file not found"
    """
    pass


def count_data(filepath: str) -> str:
    """
    Count rows, columns, and total cells in a CSV file.

    Input:
        filepath (str): Path to CSV file

    Output:
        str: Multi-line string with counts, or error message

    Examples:
        count_data('students.csv') -> "Rows: 5\nColumns: 4\nTotal Cells: 20"
        count_data('nonexistent.csv') -> "Error: file not found"
        count_data('corrupted.csv') -> "Error: invalid file format"
    """
    pass


def find_in_csv(filepath: str, search_string: str, case_insensitive: bool = False,
                columns: Optional[List[str]] = None) -> str:
    """
    Find rows containing a search string in specified columns.

    Input:
        filepath (str): Path to CSV file
        search_string (str): String to search for
        case_insensitive (bool): Whether to ignore case in search
        columns (Optional[List[str]]): List of column names/indices to search, or None for all

    Output:
        str: CSV format string with headers and matching rows, or error message

    Examples:
        find_in_csv('students.csv', 'Delhi') -> "Name,Age,City,Marks\nRavi,21,Delhi,82\nAmit,23,Delhi,77"
        find_in_csv('students.csv', 'delhi', True) -> "Name,Age,City,Marks\nRavi,21,Delhi,82\nAmit,23,Delhi,77"
        find_in_csv('students.csv', 'test', False, ['Name']) -> "Name,Age,City,Marks"
    """
    if filepath != "nonexistent.csv" and filepath != "corrupted.csv" and filepath != "empty.csv":
        with open(filepath, "r") as f:
            lines_of_file = f.readlines()
            columns_matrix = []
            for i in lines_of_file[0].split(","):
                temp_list = [i]
                a = 0
                for j in range(1, len(lines_of_file)):
                    temp_list.append((lines_of_file[j].split(","))[a])
                columns_matrix.append(temp_list)
                a += 1
            if case_insensitive == False:
                row_to_print = []
                if columns != None:
                    for i in columns_matrix:
                        if i[0] in columns:
                            for j in range(1, len(i)):
                                if i[j] == search_string or i[j] == search_string.lower() or i[j] == search_string.upper():
                                    row_to_print.append(j)
                                else:
                                    continue
                        else:
                            continue
                else:
                    for i in columns_matrix:
                        for j in range(1, len(i)):
                            if i[j] == search_string:
                                row_to_print.append(j)
                            else:
                                continue
                output_to_print = ""
                if len(row_to_print) != 0:
                    for i in row_to_print:
                        output_to_print += lines_of_file[i]
                return f"{lines_of_file[0]}{output_to_print}"
            else:
                rows_to_print = []
                if columns != None:
                    for i in columns_matrix:
                        if i[0] in columns:
                            for j in range(1, len(i)):
                                if i[j] == search_string:
                                    rows_to_print.append(j)
                                else:
                                    continue
                        else:
                            continue
                else:
                    for i in columns_matrix:
                        for j in range(1, len(i)):
                            if i[j] == search_string:
                                rows_to_print.append(j)
                            else:
                                continue
                output_to_priint = ""
                if len(rows_to_print) != 0:
                    for i in rows_to_print:
                        output_to_priint += lines_of_file[i]
                    print(output_to_print)
                return f"{lines_of_file[0]}{output_to_priint}"


def append_csv(src_file: str, dest_file: str) -> str:
    """
    Append data from source CSV to destination CSV.

    Input:
        src_file (str): Path to source CSV file
        dest_file (str): Path to destination CSV file

    Output:
        str: Success message or error message

    Examples:
        append_csv('students.csv', 'combined.csv') -> "Appended successfully."
        append_csv('students.csv', 'different_schema.csv') -> "Error: schema mismatch"
        append_csv('nonexistent.csv', 'output.csv') -> "Error: file not found"
    """
    pass


def calculate_statistics(column: str, filepath: str, operation: str) -> str:
    """
    Calculate statistical operations on a numeric column.

    Input:
        column (str): Column name or index (as string)
        filepath (str): Path to CSV file
        operation (str): Statistical operation ('mean', 'median', 'variance', 'max', 'min')

    Output:
        str: Formatted result string or error message

    Examples:
        calculate_statistics('Age', 'students.csv', 'mean') -> "21.0"
        calculate_statistics('Age', 'students.csv', 'median') -> "21"
        calculate_statistics('Name', 'students.csv', 'mean') -> "Error: cannot compute statistics on non-numeric column"
        calculate_statistics('Age', 'students.csv', 'invalid_op') -> "Error: invalid statistic operation"
    """
    pass


def print_help() -> str:
    """
    Return help message with available commands.

    Input:
        None

    Output:
        str: Multi-line help message describing all available commands

    Examples:
        print_help() -> "Available Commands:\n  -cp <src> [dest]                 Copy file\n..."
    """
    pass


def main():
    """
    Main function to handle command-line interface for csvtool.

    Input:
        Command-line arguments via sys.argv

    Output:
        Returns results to stdout or error messages

    Examples:
        python csvtool.py -count students.csv
        python csvtool.py -find students.csv "Delhi" -ic
        python csvtool.py -stats Age students.csv mean
        python csvtool.py -cp students.csv backup.csv
        python csvtool.py -append source.csv dest.csv
        python csvtool.py --help
    """
    if len(sys.argv) < 2:
        print("Usage: python csvtool.py [operation] [arguments]")
        print(print_help())
        return
    args = sys.argv[1:]
    op = args[0]
    try:
        if op == '--help' or op == 'help':
            print(print_help())
            return

        if op == '-cp':
            src = args[1]
            dst = args[2] if len(args) > 2 else None
            print(copy_file(src, dst))
            return

        if op == '-count':
            print(count_data(args[1]))
            return

        if op == '-find':
            filepath = args[1]
            search_string = args[2]
            case_insensitive = '-ic' in args
            cols = []
            start = 3
            if case_insensitive:
                ic_idx = args.index('-ic')
                start = ic_idx + 1
            if len(args) > start:
                cols = args[start:]
            print(find_in_csv(filepath, search_string,
                  case_insensitive, cols or None))
            return

        if op == '-append':
            print(append_csv(args[1], args[2]))
            return

        if op == '-stats':
            column = args[1]
            filepath = args[2]
            stat_operation = args[3]
            print(calculate_statistics(column, filepath, stat_operation))
            return

        print(f"Unknown operation: {op}")
        print(print_help())
        sys.exit(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Full traceback:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
