
from agents import Agent, Runner, trace, OpenAIChatCompletionsModel, AsyncOpenAI

class StoryAgent:
    def __init__(self):
        model = OpenAIChatCompletionsModel( 
            model="llama3.2",
            openai_client=AsyncOpenAI(base_url='http://host.docker.internal:11434/v1', api_key='')
        )
        
        self.agent_writer = Agent(
            name='story writer',
            instructions='You are a short story writer.',
            model=model,
        )

        self.agent_reviewer = Agent(
            name='grammar reviewer',
            instructions='You are a reviewer of short stories. You will be given a short story and you need to check if it is grammatically correct.',
            model=model,
        )

        self.agent_summarizer = Agent(
            name='story summarizer',
            instructions='You are a summarizer of short stories. You will be given a short story and you need to summarize it in 3 bullet points.',
            model=model,
        )
    async def run(self, topic):
        result_story = await Runner.run(self.agent_writer, 'Write a story about:' + topic)
        review = await Runner.run(self.agent_reviewer, result_story.final_output)
        result_summary = await Runner.run(self.agent_summarizer, result_story.final_output)
        
        return {
            'story': result_story.final_output,
            'review': review.final_output,
            'summary': result_summary.final_output,
        }

import asyncio

agent = StoryAgent()

async def main():
    result = await agent.run('cats')
    print("\n=== Story ===")
    print(result['story'])
    print("\n=== Grammar Review ===")
    print(result['review'])
    print("\n=== Summary ===")
    print(result['summary'])
    print("\n==============")

if __name__ == "__main__":
    asyncio.run(main())