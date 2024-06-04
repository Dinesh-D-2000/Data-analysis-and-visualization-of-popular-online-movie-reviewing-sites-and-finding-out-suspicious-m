
# Scraping the Screen: Python's Pursuit of Truth in Movie Reviews

Scraping the Screen is a data analysis and visualization project aimed at investigating the credibility of Fandango as a movie reviewing site. By scraping 500+ moview data from popular movie review sites such as Rotten Tomatoes, Metacritic, IMDB, and Fandango, this project aims to uncover any suspicious patterns in Fandango's ratings compared to other reputable sites.

## Objective

The objective of this project is to analyze and visualize historical data of movies and their ratings from various movie reviewing sites to determine if Fandango's ratings are significantly higher or biased compared to other sites.

## Tools Used

- Numpy
- Pandas
- Matplotlib
- Seaborn
- Beautiful Soup (for data scraping)

## Analysis of the Data

### Fandango Ratings
The figure shown below presents the data collected from the Fandango movie reviewing site.

<img src="https://user-images.githubusercontent.com/109975786/211799054-65044b7e-efb8-49e8-9341-8bd743e29e44.JPG">

### Other Movie Review Sites
The figure shown below presents the data collected from other movie reviewing sites such as Rotten Tomatoes, Metacritic, and IMDB.

<img src="https://user-images.githubusercontent.com/109975786/211799075-64e4fa94-1117-477c-9036-ffcc2ea3fcf0.JPG">

### Comparison of Ratings
The figure shown below compares the ratings of movies reviewed by Fandango and other reviewing sites. Fandango rates movies on a scale of 0 to 5 stars, so the ratings from other sites are also normalized to this scale for comparison.

<img src="https://user-images.githubusercontent.com/109975786/211799085-ccba824d-105c-45ad-8255-66aefaa25b7f.JPG">

### Top 10 Worst Movies
The figure shown below displays the top 10 worst movies reviewed by Fandango as well as other reviewing sites.
<img src="https://user-images.githubusercontent.com/109975786/211799103-5de0897d-b745-445d-abb0-af1a5b1e1f03.JPG">

## Visualization of the Results

The visualizations clearly indicate that Fandango tends to rate all movies highly, typically within the range of 3 to 5 stars.
<p align="center"><img src="https://user-images.githubusercontent.com/109975786/211799162-d85a2a31-465d-4876-a390-a0274f12aac4.JPG"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/109975786/211799243-79f79988-bd49-4be0-89b2-86b43dfe0cda.JPG"></p>
<img src="https://user-images.githubusercontent.com/109975786/211799891-1ff26f9b-0e51-4b85-a901-c389c784ffeb.JPG" height=300px width=200px align="center">
<img src="https://user-images.githubusercontent.com/109975786/211801190-93051f3a-686f-44de-a8e5-48511c74c71c.JPG" align="center">



For instance, "Taken 3", rated as one of the worst movies by other sites, receives a surprisingly high rating of 4.5 stars on Fandango. On average, "Taken 3" receives a rating of 1.86 from other movie reviewers, indicating a significant disparity in ratings. This serves as evidence suggesting that Fandango may indeed be a suspicious movie reviewing site.
