# Runnable 

# Tools

# Agents

# Projects



# Runnable:- 

We built a chatbot in that needs an LLM. In earlier time there were multiple LLM providers like chatgpt, antropic, grok etc. But if you want to switch between multiple chatbots you need to use their SDK and large part of code nned to be replaced.Tis problem was solved by langchain that's why developers used to love Langchain



Refer the notes for more details



Langchain introduced Pipe Operator wo connect all the components of the code instead of calling again and again each component they'll work in a flow

So chains were definitely a big improvement.

They made our code cleaner, reduced repetition, and allowed us to connect multiple components into a single

pipeline.

But as developers started building more complex applications, a new problem started to appear.

There wasn’t just one type of chain.

LangChain had introduced many different chains for different use cases.



For example:

• • LLMChain → for simple prompt + model tasks

• • SequentialChain → for multi-step workflows

• • RouterChain → for dynamic decision making

• • RetrievalQA Chain → for RAG-based applications



Now on paper, this sounds useful.

But in practice, it became confuing.

As a developer, you always had to think:

“Which chain should I use for this problem?”

And sometimes, your use case didn’t fit perfectly into any one chain.



So you either had to:

• • force your problem into an existing chain

• • or combine multiple chains in a complicated way

This made things harder instead of easier.

On top of that, chains were not very flexible.



If you wanted:

• • custom logic in between steps

• • parallel execution

• • or more control over how data flows



Chains started to feel restrictive.

So instead of simplifying things, the growing number of chains actually created confusion and friction for

developers.

And because of all these limitations, LangChain made an important decision.

They moved away from the concept of predefined chains and introduced a much more flexible system... Runnables



Now this is where things become really interesting.

Instead of having different types of chains for different use cases, LangChain introduced a much simpler

and more powerful idea.

They said what if every component we are using is treated the same way?

Think about it.

We already have multiple components in our application:

we have prompt templates, we have models, we have output parsers, retrievers, and even custom functions.

Now instead of treating all of these differently, LangChain introduced a unified concept...

Everything is a Runnable.

That means:

your prompt template is a runnable,

your model is a runnable

your output parser is a runnable,

even your own Python function can be a runnable.

So instead of thinking in terms of different types of chains, now you just think in terms of runnables that

can be connected together.



Now imagine all these components as Lego blocks.

Each block has its own purpose. One block might be a prompt template, another might be a model, another could

be an output parser, and so on.

Individually, they all do different things.

But here’s the interesting part...

No matter what the block does, the way you connect one block to another is always the same.

Just like Lego.

You don’t need a different way to connect different pieces. Every block follows the same connection structure.

And that’s exactly what LangChain did with runnables.



Now there’s one really interesting thing about runnables.

All these different components, whether it’s a prompt template, a model, an output parser, or even your own

function, they all expose the same kind of methods.

For example, you’ve already seen one of them:

👉 invoke()

This is used to run the component on a single input and get the output.

But that’s not the only one.

You also have:

batch() when you want to process multiple inputs at once

stream() when you want to get output token by token like real-time responses

Now think about this...

Completely different components, doing completely different tasks, but all of them can be used in the exact same

way.

And that is the real power here.

You don’t need to learn different ways to use different components. Once you understand how one runnable

works, you can use any other runnable the same way.



Actual Runnables

These are your components/runnables:

• • LLM

• • Prompt Template

• • Output Parser

• • Retriever

• • Tools

Basically: they do the actual job



## Runnable Sequence

Now that we understand what runnables are, let’s see how we actually use them in real applications.

We’re going to learn this in three simple steps.

First, we’ll start with the most basic and most important pattern a simple sequence.

In this, we just connect components like a pipeline. The output of one component becomes the input of the

next. So your flow becomes something like prompt to model to parser. This is the foundation, and honestly,

most applications start like this.



## Parallel Runnable

Now till this point, we have only seen how to build a single pipeline where the input flows step by step and

produces one output. But in real-world applications, sometimes we don’t want just one result. We might want

multiple outputs at the same time, like a short explanation and a detailed explanation, or maybe the same answer

in different formats. Instead of running the pipeline again and again for each case, we can use a Parallel

Runnable.

In this approach, we define multiple pipelines inside a dictionary, and all of them run simultaneously on the

same input. Each pipeline produces its own output, and in the end, we get all the results together in a structured

form. So instead of one input giving one output, now one input can give multiple outputs in a single execution,

which makes our applications more powerful and efficient.



## Runnable Lambda

Now sometimes in our pipeline, we don’t just want to pass data forward, we might want to slightly modify it or pick

a specific part of it before sending it to the next step. This is where RunnableLambda comes in. It allows us to write

a simple Python function and insert it inside our pipeline as a runnable. For example, if our input is a dictionary with

multiple keys, and we only want to send one specific part of it to a particular pipeline, we can use RunnableLambda

to extract that part. So instead of the entire input going everywhere, we can control exactly what each component

receives. In simple terms, RunnableLambda lets us add custom logic inside our runnable flow, making our pipelines

more flexible and powerful.



## Runnable Passthrough

Runnable Passthrough is used when we want to keep the original input or some intermediate data while passing it

through the pipeline. Normally, in a sequence, each step replaces the previous output, so earlier data gets lost. But in

many real-world scenarios, we need to carry multiple pieces of information together. RunnablePassthrough allows us to

forward the input as it is, without modifying it, so that it can be used along with other outputs in later steps. In simple

terms, it helps us preserve data while still continuing the flow of the pipeline.



# Tools:-

An LLM (Large Language Model) is an

AI system trained to understand and

generate human language.



Thinks and gives output



LLM is not good at real time data => LLM is trained on previous data => cant do reliable calculations 



LLM cant call APIS



Dont know about your personal data



Booking system, ticket system



Tools are simply functions or external services that an LLM can use to do real-world tasks. On its own, an LLM

can only generate text, but with tools it can fetch live data, perform accurate calculations, access databases, or

execute actions. In short, tools extend an LLM from just thinking to actually doing things.



We use an LLM as the brain, tools to perform tasks, and our code

to define the logic together, this creates an agent.



###### **LLM decides what to do,**

###### **tools help do the task,**

###### **and our code controls how everything works together.**

###### 

###### **Agent = Brain (LLM) + Tools + Control Logic (our code)**



Tools are used to make agents



#### Tools Category

=> Built in Tools => Built-in tools are tools that are already provided by a framework, so you don’t have to create them from scratch. They are ready to use and help the LLM perform common tasks like searching the internet, doing calculations, or working with data. You just connect them to your LLM, and it can start using them easily.



=> Custom Tools => Custom tools are tools that you create yourself based on your needs. They are usually simple functions written in code that help the LLM perform specific tasks, like accessing your database, processing your data, or calling your own APIs. This allows you to give the LLM exact abilities that match your project.



llm and tool connecting



1. Tool creation
2. Tool Binding
3. Tool Calling
4. Tool Execution



when you bind a tool with llm so the input token increase in meta data

tool is not an agent



