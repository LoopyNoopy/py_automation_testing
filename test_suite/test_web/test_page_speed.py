import allure
import pytest
import requests
import time
from test_suite.driver_functions import *


# Function to get PageSpeed Insights data
def get_pagespeed_insights(url, strategy, categories=None):
    with allure.step(f"Getting response from PageSpeed Insights"):
        endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
        params = {
            'url': url,
            'key': 'AIzaSyAYFmW25I_WJqRpiuMeQBtAN-TkiUpF0xI',
            'strategy': strategy  # 'mobile' or 'desktop'
        }
        if categories:
            params['category'] = categories  # Add the categories if specified

        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None
        return response.json()


# Function to get the score from the insights
def get_insights(url, strategy, category, retries=3):
    with allure.step(f"Getting score for {category} on {strategy}"):
        for attempt in range(retries):
            data = get_pagespeed_insights(url, strategy, category)
            if data is None:
                print(f"Attempt {attempt + 1} failed: No data received.")
                time.sleep(2)  # Wait before retrying
                continue

            lighthouse_result = data.get('lighthouseResult', {})
            categories = lighthouse_result.get('categories', {})
            score = categories.get(category, {}).get('score', None)
            if score is not None:
                return score

        print(f"Attempt {attempt + 1} failed: No score found for {category}. Response: {data}")

    return None


# Parameterize the strategy and categories
@allure_suite("Silhouette Web", "Page Speed", "Search Engine Optimisation")
@allure_story("Silhouette Web","Website Performance","Page Speed Insights")
@allure_attributes(
    "This is checking to see if the score for performance, accessibility, seo and best practices score a number higher than 90",
    ["Page Speed Insights"],
    allure.severity_level.TRIVIAL,
    "Daniel Burgess"
)
@allure.link("https://pagespeed.web.dev/", name="PageSpeed Insights")
@pytest.mark.parametrize("strategy", ["mobile", "desktop"])
@pytest.mark.parametrize("category", ["performance", "accessibility", "best-practices", "seo"])
def test_pagespeed_insights(strategy, category, web_url):
    allure.dynamic.title(f'Testing {category} score on {strategy}')
    allure.dynamic.tag(category,strategy)
    score = get_insights(web_url, strategy, category)
    assert score is not None, f"No score found for {category} on {strategy} strategy"
    score_percentage = score * 100
    assert 90 <= score_percentage <= 101, f"Score for {category} on {strategy} strategy is out of expected range: {score_percentage}"

