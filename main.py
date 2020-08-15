from services.twitter.twitter_service import TwitterService


def main():
    twitter_service = TwitterService()
    hash_tags = ['#python', '#angular', '#programming', '#typescript', '#node']

    for hash_tag in hash_tags:
        twitter_service.retweet_by_query(hash_tag, 10)


if __name__ == '__main__':
    main()
