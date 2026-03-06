# ShoeBox — Dropshipping Product Discovery Platform

A Python-based web scraping and dashboard application that aggregates discounted shoe deals from major retailers, built to give local dropshippers a competitive edge in their market.

---

## The Problem

Local dropshippers in South Africa traditionally rely on a tedious, manual product research process — browsing retailer websites, taking screenshots of sale items, and posting them individually to their social media platforms. This approach is time-consuming, inconsistent, and makes it difficult to compete with established second-hand clothing sellers and factory-reject vendors who already have streamlined supply chains.

ShoeBox was built to solve this. Instead of manually hunting for deals, dropshippers and their customers get instant access to a centralized, always-current feed of quality shoes on sale from top retailers — giving them a real competitive edge.

---

## How It Works for Users

ShoeBox puts the product discovery process on autopilot:

1. **Browse** — Customers visit the ShoeBox dashboard and scroll through discounted shoes aggregated from Nike and Bash.com.
2. **Choose** — When a customer finds a shoe they're interested in, they click through directly to the product's official retailer page to view full details (sizes, colors, availability).
3. **Order** — From there, either:
   - The customer places the order directly and the dropshipper handles delivery, **or**
   - The customer shares the shoe's details (size, color, etc.) with the dropshipper, who then handles both the purchase and delivery on their behalf.

This removes the back-and-forth of manual product sharing and gives customers a professional, browsable storefront rather than a stream of screenshots.

---

## Features

- **Multi-Source Scraping**: Automatically pulls discounted shoes from Nike (ZA) and Bash.com
- **Centralized Dashboard**: Clean, browsable Flask web interface — no social media scrolling required
- **Direct Retailer Links**: Every product links directly to its official page for accurate sizing and stock info
- **Discount Visibility**: Displays sale price, original price, and percentage off at a glance
- **Pagination**: Browse 30 products per page with smooth navigation
- **Source Attribution**: Each product is labeled by its retailer

---

## Tech Stack

| Layer             | Technology               |
| ----------------- | ------------------------ |
| Language          | Python 3                 |
| Web Framework     | Flask                    |
| Scraping          | BeautifulSoup4, Requests |
| Data Handling     | Pandas                   |
| Templating        | Jinja2                   |
| Production Server | Gunicorn                 |
| Parser            | LXML                     |

---

## Installation

### Prerequisites

- Python 3.7+
- pip
- Virtual environment (recommended)

### Setup

1. **Clone the repository**

   ```bash
   cd Dropshipping_Scrapper
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Step 1 — Run the Scrapers

```bash
python scrapers/nike_scraper.py
python scrapers/bash_scraper.py
```

### Step 2 — Combine the Data

```bash
python combineScrappedInfo.py
```

This merges both scraper outputs into a single `shoes.csv` file.

### Step 3 — Launch the Dashboard

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## Project Structure

```
Dropshipping_Scrapper/
├── app.py                      # Flask web application
├── combineScrappedInfo.py      # Data aggregation script
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── README.md                   # This file
├── shoes.csv                   # Combined scraped data (generated)
├── scrapers/
│   ├── nike_scraper.py        # Nike ZA scraper
│   ├── bash_scraper.py        # Bash.com scraper
│   ├── nike_shoes.csv         # Nike output
│   └── bash_shoes.csv         # Bash output
├── templates/
│   └── index.html             # Dashboard HTML template
└── static/
    ├── styles.css             # Stylesheet
    └── images/                # Logo and static assets
```

---

## Configuration

- **Bash pages scraped**: In `bash_scraper.py`, adjust `start_page` and `end_page` to control how many pages are scraped
- **Items per page**: In `app.py`, modify the `PER_PAGE` variable

---

## Development Workflow

This project follows a Git feature-branch workflow. The pagination feature serves as a documented example:

```bash
# Create a feature branch
git checkout -b feature/pagination

# After implementing and testing:
git add .
git commit -m "Add pagination feature to dashboard"
git push origin feature/pagination

# Merge via Pull Request, then clean up
git branch -d feature/pagination
git push origin --delete feature/pagination
```

**Branch naming convention:**

- `feature/` — new features
- `bugfix/` — bug fixes
- `hotfix/` — critical production fixes
- `refactor/` — code improvements

---

## Runner Fee Structure

ShoeBox displays a **ShoeBox Price** alongside the retailer's sale price. This ShoeBox Price includes a flat runner fee that covers the dropshipper's service and delivery handling.

### Fee Tiers

| Retailer Sale Price | Runner Fee | Why                                             |
| ------------------- | ---------- | ----------------------------------------------- |
| Under R300          | +R50       | Budget items — low fee keeps them accessible    |
| R300 – R699         | +R70       | Mid-range items                                 |
| R700 – R1,499       | +R99       | Core catalog range (most Nike & Bash items)     |
| R1,500 and above    | +R120      | Premium items — customer expects a service cost |

### How it's calculated

In `app.py`, the `parse_price()` function handles both South African price formats used by Nike and Bash (they differ in how they use commas and periods). The `calculate_runner_fee()` function then applies the correct tier and passes a `shoebox_price` and `runner_fee` value to the template for each product.

### Design rationale

A tiered flat fee was chosen over a percentage markup because:

- It's transparent — customers can see exactly what the runner fee is
- It keeps budget items (under R300) accessible while still being profitable
- It scales predictably without making premium items feel overpriced

---

## Future Enhancements

- Add more South African retailer sources
- Replace CSV storage with a database (PostgreSQL or SQLite)
- Add search, filter, and sort functionality
- Automate daily scraping on a schedule
- Display price history and trend graphs
- Add a customer wishlist / saved items feature

---

## Notes on Web Scraping

- Always respect a website's `robots.txt` and Terms of Service
- Use descriptive `User-Agent` headers to identify your scraper
- Implement rate limiting to avoid overloading servers
- For JavaScript-heavy sites, consider using Selenium

---

## License

AIMS Scholarship Project

## Author

Tlhokomelo Mohobane
