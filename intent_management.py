def list_intent(project_id):
    """

    list up dialogflow intents

    :param project_id: str
    :return: None

    """
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)

    intents = intents_client.list_intents(parent)

    for intent in intents:
        print('=' * 20)
        print(f'Intent name: {intent.name}')
        print(f'Intent display_name: {intent.display_name}')
        print(f'Action: {intent.action}\n')
        print(f'Root followup intent: {intent.root_followup_intent_name}')
        print(f'Parent followup intent: {intent.parent_followup_intent_name}\n')

        print('Input contexts:')
        for input_context_name in intent.input_context_names:
            print(f'\tName: {input_context_name}')

        print('Output contexts:')
        for output_context in intent.output_contexts:
            print(f'\tName: {output_context.name}')


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """

    Create on intent of the given intent type.

    :param project_id:  str
    :param display_name:  str
    :param training_phrases_parts: List[str]
    :param message_texts:  List[str]
    :return: None

    """

    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    # print(training_phrases_parts)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(parent, intent)

    print(f"Intent created: {response}")

