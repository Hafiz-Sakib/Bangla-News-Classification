# Text Classification of Bangla News Articles Using Recurrent Neural Networks (RNN)

This repository contains resources and code for classifying Bangla news articles using Recurrent Neural Networks (RNN). The project focuses on building a text classification model to categorize news articles into topics such as Economy, Entertainment, International, Sports, and State.

## Project Structure

- `Dataset CSV/`: Contains the main dataset in CSV format (`news_dataset.csv`).
- `Datasets TXT Files/`: Contains raw text files for each category (Economy, Entertainment, International, Sports, State).
- `TXT to CSV Converter Code/`: Includes code (`convert.py`) to convert TXT files into CSV format for model training.
- `datasets_for_text_classification.txt`: Documentation or notes about datasets used.

## Features

- Preprocessing of Bangla news articles
- Conversion of raw TXT files to CSV
- RNN-based text classification model
- Multi-category classification (Economy, Entertainment, International, Sports, State)

## Getting Started

1. **Prepare the Dataset**

   - Use the TXT files in `Datasets TXT Files/` or the CSV in `Dataset CSV/`.
   - If needed, run `convert.py` to convert TXT files to CSV.

2. **Model Training**
   - Implement and train an RNN model using the prepared dataset.
   - Evaluate the model on test data.

## Requirements

- Python 3.x
- Common libraries: pandas, numpy, tensorflow/keras, scikit-learn

## Usage

1. Clone the repository:
   ```powershell
   git clone https://github.com/Hafiz-Sakib/Text-Classification-of-Bangla-News-Articles-Using-Recurrent-Neural-Networks-RNN-.git
   ```
2. Prepare your environment and install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the converter (if needed):
   ```powershell
   python TXT to CSV Converter Code/convert.py
   ```
4. Train your model using the dataset.

## Folder Details

- **Dataset CSV/**: Contains the main CSV dataset.
- **Datasets TXT Files/**: Raw news articles organized by category.
- **TXT to CSV Converter Code/**: Script for converting TXT files to CSV.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Author

- Mohammad Hafizur Rahman Sakib
- Arnab Shikder
- Shuvra Roy
