#pip install streamlit
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.title("Generate Marketing Plan 🐦")
st.subheader("🚀 Generate marketing plan for a product")
gpt3_model = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

product = st.text_input("Product name")
simple_prompt = """
                    Write a marketing plan for a new product
                """
instruction_prompt = """
                        Write a comprehensive marketing plan for a new {product}. The plan should include the following sections:

1. **Executive Summary**: A brief overview of the marketing strategy, key objectives, and goals for the {product}.

2. **Market Research**:
   - **Target Audience**: Describe the primary demographics, needs, and preferences of the target market.
   - **Market Analysis**: Include information on market size, growth potential, and trends relevant to the {product}.

3. **Competitive Analysis**:
   - **Competitor Overview**: Identify key competitors and analyze their strengths and weaknesses.
   - **Differentiation**: Explain how the new {product} stands out from the competition.

4. **Marketing Strategy**:
   - **Positioning**: Define the {product}'s positioning in the market.
   - **Value Proposition**: Articulate the unique benefits and value that the {product} offers to customers.
   - **Pricing Strategy**: Outline the pricing model and rationale.

5. **Marketing Channels**:
   - **Digital Marketing**: Strategies for online presence, including social media, SEO, and email marketing.
   - **Traditional Marketing**: Approaches for print, TV, or radio advertising if applicable.
   - **Sales Strategy**: Tactics for direct sales, partnerships, or distribution.

6. **Action Plan**:
   - **Timeline**: Provide a timeline for key marketing activities and milestones.
   - **Budget**: Detail the budget allocation for different marketing activities.

7. **Metrics and Evaluation**:
   - **KPIs**: Define key performance indicators to measure the success of the marketing plan.
   - **Monitoring**: Describe how the effectiveness of the marketing plan will be monitored and adjusted.

Ensure that the plan is detailed, actionable, and tailored to the specific {product} and market conditions.

                     """
combined_prompt = f"{simple_prompt}\n\n{instruction_prompt.format(product=product)}"
if st.button("Generate"):
    response = gpt3_model.invoke(combined_prompt)
    st.write(response.content)

# python test.py