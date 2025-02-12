###
#Automated RSS Feed example
#Creates an RSS feed updating every 3 minutes with "Hello World [i]" messages.
###

import time
from feedgen.feed import FeedGenerator
import os

# Define RSS file path
rss_file = "updates.xml"

# Create or load the RSS feed
fg = FeedGenerator()
fg.title("Hello World RSS Updates")
fg.link(href="http://localhost:8000/updates.xml", rel="self")
fg.description("Automated RSS Feed updating every 3 minutes.")

# Incremental counter
counter = 1
run_time = 20 * 60  # Run for 20 minutes
interval = 3 * 60  # Update every 3 minutes
start_time = time.time()

while time.time() - start_time < run_time:
    print(f"Hello World [{counter}]")  # Print to console

    # Add a new RSS entry
    entry = fg.add_entry()
    entry.title(f"Hello World Update {counter}")
    entry.description(f"This is update number {counter}.")
    entry.link(href="http://localhost:8000/updates.xml")

    # Save the updated RSS feed
    fg.rss_file(rss_file)

    print(f"RSS feed updated: {rss_file}")
    counter += 1

    time.sleep(interval)  # Wait 3 minutes before next update
