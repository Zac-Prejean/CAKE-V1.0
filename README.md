# CAKE-V1.0
This code is a comprehensive script designed for handling order processing, image generation, and PDF creation for a system used in e-commerce and order fulfillment. Here's a detailed breakdown of what each part does:

# Functions

 

    generate_custom_id_tag:
        Generates a unique custom ID tag based on the current date and a random 4-digit number.
        Ensures the random number is unique by checking a set of used numbers.
    create_txt_file:
        Creates a text file containing order details and writes it to both a specified output folder and an archive folder.
    process_csv:
        Reads a CSV file and processes each row to fetch order images using the get_order_images function.
    get_order_images:
        Makes an API call to fetch order details.
        Downloads images for items matching a specific store name ("Zazzle" in this case).
    download_images:
        Downloads images based on specific conditions and file naming conventions.
    download_png:
        Downloads PNG images from a URL and saves them to a specified location.

# Flask Application

 

    Setup:
        Configures a Flask application with SQLAlchemy for database interactions.
        Defines models such as ScannedNumber to store scanned numbers.
    Routes:
        Various routes for handling different functionalities such as:
            Admin interface (/admin)
            Password checking (/check_password)
            CSV processing (/run-script)
            Label generation (/designer)
            Status updates (/update_status, /update_all_items_status)
            File management (/get_txt_files, /delete_combined_csv)
            Order processing (/process_xlsx)
            Scan-in and scan-out stations (/scanIn, /scanOut)
            File serving (/designed_status.txt, /dtg_item_description.json, /images/<path:filename>)

# Image and PDF Generation

 

    add_order_number_to_blabel_pdf:
        Adds order details to a specific PDF template for "BLABEL" orders.
        Handles QR code generation and text drawing on the PDF.
    create_labels:
        Creates labels for different types of orders ("BLABEL", "CLABEL", etc.).
        Downloads images based on URLs specified in the order options.
    process_row:
        Processes each row from the CSV file to handle image generation and label creation.
    export_images:
        Main function to export images and create PDFs for the orders.
        Calls other functions to handle specific tasks like creating pick lists.
    create_pick_list_pdf:
        Generates a pick list PDF based on the processed order data.
        Merges the generated content with a background PDF template.

# Utility Functions

 

    appendrow:
        Appends a row to a CSV file if it doesn't already exist.
    remove_duplicates:
        Removes duplicate rows from a CSV file.
    order_details:
        Makes an API call to fetch order details and appends them to a CSV file.
    process_xlsx:
        Processes an Excel file to convert it to a CSV file ready for label generation.

# Execution

    The script sets up and runs a Flask web server when executed directly, making the application available at http://127.0.0.1:5000.

    Overall, this script is a complex and comprehensive tool for managing and processing orders, generating labels, handling images, and creating necessary PDFs for order fulfillment processes. It includes web-based interaction using Flask and extensive file handling and processing capabilities.
