from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub   
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()


def main():

    huggingfacehub_api_token = os.getenv('HUGGINGFACE_TOKEN')
    sql_llm = HuggingFaceHub(
                repo_id="mrm8488/t5-base-finetuned-wikiSQL",
                huggingfacehub_api_token=huggingfacehub_api_token
               )

    eng_llm = HuggingFaceHub(
                repo_id="mrm8488/t5-base-finetuned-wikiSQL-sql-to-en",
                huggingfacehub_api_token=huggingfacehub_api_token
               )

    prompt = PromptTemplate(
                input_variables=["question"],
                template="Translate English to SQL: {question}"    
                )

    sql_chain = prompt | sql_llm
    eng_chain = prompt | eng_llm    
    
    print("Welcome to the SQL Query Generator CLI!")
    print("Type 'exit' to quit.\n")
    
    query_type = input("Do you want to generate SQL query or translate query to english? (sql/english): ").strip().lower() 
    while query_type not in ["sql", "english"]:
        if query_type  == "exit":
            print("Goodbye!")
            return
        print("Invalid input. Please enter 'sql' or 'english'.")
        query_type = input("What query type would you like to generate? (sql/english): ").strip().lower()

    # CLI Loop
    while True:
        user_input = input("Enter your question: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            return
                                                                
        try:
            # Process the input through the chain
            if query_type == "sql":
                sql_query = sql_chain.invoke({"question": user_input})
                print(f"Generated SQL Query:\n{sql_query}\n")
            elif query_type == "english":
                eng_query = eng_chain.invoke({"question": user_input})
                print(f"Explanation for the SQL query:\n{eng_query}\n")
            
            switch = input("Do you want to switch query types? (yes/no): ").strip().lower()
            if switch == "yes":
                query_type = input("Do you want to generate SQL query or translate query to english? (sql/english): ").strip().lower()

                while query_type not in ["sql", "english"]:
                    if user_input.lower() == "exit":
                       print("Goodbye!")
                       return 

                    print("Invalid input. Please enter 'sql' or 'english'.")
                    query_type = input("What query type would you like to generate? (sql/mongo): ").strip().lower()
            elif switch == "exit":
                print("Goodbye!")
                return

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
