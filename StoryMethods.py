class StoryMethods:
    
    def story_ai(msg):
        story_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system", 
                "content": """You are a bestseller story writer.
                            You'll take user's prompt and generate a 100 words shortstory for children age 8-10"""
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

    def cover_ai(msg):

        cover_response = client.images.generate(
        model="dall-e-3",
        prompt=f"{msg} in ghlibli style",
        size="1024x1024",
        quality="standard",
        n=1,
        )

        image_url = cover_response.data[0].url
        #display(Image(url=image_url))

        return image_url
    
    def design_ai(msg):
        
        design_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                
                "role": "system", 
                "content": """Base on the story given. 
                            You will design a detailed image prompt for the cover image of this story.
                            The image prompt should include theme of the story with relevant color,
                            suitable for children book.
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
    