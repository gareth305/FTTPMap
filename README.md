# 🚀 **FTTPMap: Mapping the Future of Fibre**

Welcome to **FTTPMap**—a project born out of frustration with the slow and unclear rollout of FTTP (Fibre to the Premises). If you're tired of waiting and wondering about fibre availability in your area, you're not alone. One Sunday afternoon, I decided to take matters into my own hands and build a map that shows where CityFibre has (or hasn’t) rolled out FTTP. While it’s not pinpoint accurate, it does provide a **general idea** of FTTP availability in the specified area.
![2024-08-11 19_11_21-](https://github.com/user-attachments/assets/2f8d3841-4586-44e5-b38f-0051c957c20c)

---

## 🔍 **Why FTTPMap?**

The inspiration for FTTPMap came from my own need for information. Like many, I was frustrated by the lack of transparency and progress in the FTTP rollout. **FTTPMap** is my attempt to bridge that information gap, providing a rough but helpful overview of fibre availability.

---

## ⚙️ **How It Works**

FTTPMap leverages Python scripts to gather and display data in three steps:

1. **📌 Querying the UPRN Register:**  
   The journey begins by querying the UPRN (Unique Property Reference Number) register for specific postcodes.

2. **🛠 Scraping CityFibre's FTTP Checker:**  
   The UPRNs are then used to scrape data from CityFibre’s FTTP availability checker, revealing where fibre is available.

3. **🌍 Mapping the UPRNs:**  
   Finally, we retrieve the latitude and longitude of these UPRNs, allowing us to plot their locations on the map for easy visualization.

---

## 🎨 **A Hobbyist's Creation**

*FTTPMap is not a professional-grade tool, and it might not follow the latest coding best practices.* This project is something I built as a hobby, out of a personal need. There are undoubtedly more efficient ways to achieve this, but FTTPMap gets the job done and provides a valuable resource for those curious about fibre availability.

---

## 🛠 **Behind the Scenes**

To make FTTPMap functional, a few key scripts and tools are at play:

- **`fttp.py`**  
  This script queries the endpoints and scrapes the data, writing it to a CSV file each time it moves to the next postcode. It ensures that all relevant data is captured efficiently.

- **`httpserver.py`**  
  Acting as a simple web server, this script serves the CSV file along with the images. It was designed to be a straightforward solution that requires little configuration but can handle CORS (Cross-Origin Resource Sharing) requests.

- **`fttpvisual.html`**  
  This HTML file visualizes the data by utilizing **PapaParse**, **Leaflet**, and **OpenStreetMaps**. Together, these tools bring the FTTP availability data to life on an interactive map.

---

## 🛠 **Installation Instructions**

To get started with FTTPMap, follow these steps:

1. **Install Requirements**
    - Ensure you have Python 3 installed on your system.
    - Install the necessary libraries by running:
      ```bash
      pip install beautifulsoup4
      ```

2. **Run `httpserver.py`**
    - In your terminal, navigate to the project directory and run:
      ```bash
      python httpserver.py
      ```

3. **Modify `fttp.py`**
    - Open `fttp.py` in your preferred text editor.
    - On **line 6**, list the postcodes you want to search for inside the square brackets. Postcodes should be formatted like `['xx22xxx', 'xx33xxx', ...]`.
    - **Tip:** You can retrieve multiple postcodes using [FreeMapTools](https://www.freemaptools.com/find-uk-postcodes-inside-user-defined-area.htm) to list all the postcodes in a drawn area. Ensure the postcodes have no spaces.

4. **Run `fttp.py`**
    - Open a second terminal and run:
      ```bash
      python fttp.py
      ```

5. **Open `fttpvisual.html`**
    - Now, open `fttpvisual.html` in your web browser. As the postcode queries complete, refreshing the page will plot them on the map.

---

**Enjoy exploring FTTPMap, and here’s to hoping for a faster fibre future!**
