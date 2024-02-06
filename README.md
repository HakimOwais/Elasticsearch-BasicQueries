# Elasticsearch-JobRecommendation-SearchEngine


## Notebook Title: Exploratory Data Analysis, Text Embeddings and Vector Similarity Search

### Overview:

This Jupyter Notebook performs Exploratory Data Analysis (EDA) on a job dataset and utilizes the Sentence Transformers library to create text embeddings for job descriptions. The analysis includes visualizations of employment type distribution and summary statistics for numerical columns.
Libraries Used:

    numpy: For numerical operations.
    pandas: For data manipulation and analysis.
    matplotlib and seaborn: For data visualization.
    nltk: For natural language processing tasks.
    re: For regular expressions.
    sentence_transformers: For creating sentence embeddings.

### Steps in the Notebook:
1. Importing Necessary Libraries:

    Importing essential libraries such as numpy, pandas, matplotlib, seaborn, and others.

2. Loading and Filtering Data:

    Loading the job dataset from 'Combined_Jobs_Final.csv'.
    Selecting relevant columns for analysis.

3. Summary Statistics:

    Calculating summary statistics for numerical columns using describe().

4. Employment Type Analysis:

    Analyzing the distribution of employment types.
    Visualizing the distribution using a bar plot.

5. Text Cleaning and Embeddings:

    Implementing text cleaning functions to preprocess job descriptions.
    Utilizing Sentence Transformers to generate embeddings for job descriptions.

### Functions:
cleaning(txt):

    Performs text cleaning on the input text.
    Removes non-alphanumeric characters, tokenizes, converts to lowercase, removes English stopwords, performs stemming, and joins the cleaned words.

### External Libraries:
Sentence Transformers:

    Used for creating embeddings of job descriptions.


## Vector Similarity Search for Jobs (Elasticsearch)

### Overview:

This Python script utilizes the Elasticsearch engine to index and search job descriptions based on a given input keyword. The script includes the following key functionalities:

    Connecting to an Elasticsearch instance.
    Creating an index with mappings using a specified index mapping (indexMapping).
    Indexing job records from a DataFrame (df) into the Elasticsearch index.
    Performing a k-NN search to find similar job descriptions based on an input keyword.

### Steps in the Script:

1. Connecting to Elasticsearch:

    Establishing a connection to the Elasticsearch instance running at http://localhost:9200.

2. Creating Index and Mappings:

    Creating an index named "job_description" with mappings defined in the indexMapping module.

3. Indexing Job Records:

    Converting DataFrame records to a list of dictionaries.
    Indexing each job record into the "job_description" index in Elasticsearch.

4. k-NN Search:

    Encoding the input keyword using the Sentence Transformers model.
    Performing a k-NN search to find similar job descriptions based on the input keyword.
    Returning the top hits including the job titles and descriptions.

### External Modules:
indexMapping Module:

    Contains the index mapping for the Elasticsearch index.

