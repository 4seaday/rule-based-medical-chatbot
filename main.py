import pandas as pd
from intent_management import list_intent, create_intent
from utils import Params

def main():
    params = Params('config/params.json')
    df = pd.read_csv('./data/200219_medical_chat_qa.csv')
    df = df.head(5)

    for idx, data in df.iterrows():
        display_name = f"test_{idx+5}"
        create_intent(params.project_id, display_name, [data['question']], [data['answer']])


if __name__ == '__main__':
    main()