from src.linkedin_bot import LinkedInBot

if __name__ == "__main__":
    bot = LinkedInBot()
    bot.login()

    locations = [
        #"India", "Colombia", "Argentina", "Ukraine",
        #"Istanbul", "United States",
        "Spain", "Italy"
    ]

    profiles = bot.search_recruiters(
        keyword="Tech Recruiter",
        locations=locations
    )

    # for link in profiles:
    #     print(link)

    # bot.close()
