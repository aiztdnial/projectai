class StoryMethods:
    
    def story_ai(msg,client):
        story_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system", 
                "content": """You are a professional hairstyler and fashion designer for men.
                            You'll take user's prompt and give an advice to user about hairstyle based on their face structure and fashion that are suitable for them for a certain occasion."""
                },
                {
                "role": "user", 
                "content": f'{msg}'
                }
            ],
            max_tokens= 400,
            temperature=1.3
        )

        story = story_response.choices[0].message.content
        #print(story)

        return story

    def cover_ai(msg,client):

        cover_response = client.images.generate(
        model="dall-e-3",
        prompt=f"{msg} real life style",
        size="1024x1024",
        quality="standard",
        n=1,
        )

        uploaded_files = cover_response.data[0].url
        #display(Image(url=image_url))

        return uploaded_files
    
    def design_ai(msg,client):
        
        design_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                
                "role": "system", 
                "content": """Based on the criteria given. 
                            You will design a detailed image prompt based on user's face structure.
                            The image prompt should include the hairstyle that suitable for them,
                            outfit based on you have advised.
                            The output should be within 100 characters"""
                },
                {
                "role": "user", 
                "content": f'{msg}'
                }
            ],
            max_tokens= 100,
            temperature=1.3
        )
        design_prompt = design_response.choices[0].message.content
        #print(design_prompt)

        return design_prompt
    