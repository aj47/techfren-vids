import autogen
llm_config = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")
user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
   human_input_mode="TERMINATE"
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
code_reviewer = autogen.AssistantAgent(
    name="Code_Reviewer",
    system_message="Reviews code by Coder",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, code_reviewer], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
user_proxy.initiate_chat(manager, message="create a snake game")