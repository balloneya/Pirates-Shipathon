def parse_line(line):
    parts = line.split("\n")
    if not parts:
        return None, None, None, None, None, None, "-> Empty line"
    usser = None
    movie_name = None
    ratingg = None
    date_of_review = None
    tiime = None
    comment_of_picture = None
    for item in parts:
        try:
            key, value = item.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "User":
                usser = value
            elif key == "Movie":
                movie_name = value
            elif key == "Date":
                date_of_review = value
            elif key == "Rating":
                try:
                    ratingg = int(value)
                except:
                    pass
            elif key == "Time":
                tiime = value
            elif key == "Comment":
                comment_of_picture = value
        except ValueError:
            pass
    error_message = None
    if usser == None and movie_name == None and ratingg == None and date_of_review == None:
        error_message = "-> missing all crucial elements(user, movie name, rating and date of review)"
    elif usser == None and movie_name == None and ratingg == None:
        error_message = "-> missing user, movie name and rating"
    elif usser == None and movie_name == None and date_of_review == None:
        error_message = "-> missing user, movie name and date of review"
    elif usser == None and ratingg == None and date_of_review == None:
        error_message = "-> missing user, rating and date of review"
    elif movie_name == None and ratingg == None and date_of_review == None:
        error_message = "-> missing movie name, rating and date of review"
    elif usser == None and movie_name == None:
        error_message = "-> missing user and movie name"
    elif usser == None and date_of_review == None:
        error_message = "-> missing user and date of review"
    elif usser == None and ratingg == None:
        error_message = "-> missing user and rating"
    elif movie_name == None and ratingg == None:
        error_message = "-> missing movie name and rating"
    elif movie_name == None and date_of_review == None:
        error_message = "-> missing movie name and date of review"
    elif ratingg == None and date_of_review == None:
        error_message = "->missing rating and date of review"
    elif usser == None:
        error_message = "->missing user"
    elif movie_name == None:
        error_message = "-> missing movie name"
    elif ratingg == None:
        error_message = "-> missing rating"
    elif date_of_review == None:
        error_message = "-> missing date of review"
    return usser, movie_name, date_of_review, tiime, ratingg, comment_of_picture, error_message


def process_file(filename):
    valid_reviews = []
    invalid = []
    summary = []
    movies = []
    dates = []
    users = []
    average_rating_of_movies = []
    ratings_of_users = []
    dates_with_review_number = []
    sentiment_calculation = []
    with open(f"../{filename}", "r") as f:
        content = f.read()
        separate_reviews = content.split("--- REVIEW END ---")
        print(separate_reviews)
        for review in separate_reviews:
            if review.strip():
                user, movie, date, time, rating, comment, error = parse_line(
                    review)
                if user != None and movie != None and rating != None and date != None:
                    if time != None and comment != None:
                        dict_of_review = {
                            "user": user,
                            "movie": movie,
                            "date": date,
                            "time": time,
                            "rating": rating,
                            "comment": comment
                        }
                    elif time == None and comment != None:
                        dict_of_review = {
                            "user": user,
                            "movie": movie,
                            "date": date,
                            "rating": rating,
                            "comment": comment
                        }
                    elif comment == None and time != None:
                        dict_of_review = {
                            "user": user,
                            "movie": movie,
                            "date": date,
                            "time": time,
                            "rating": rating
                        }
                    elif time == None and comment == None:
                        dict_of_review = {
                            "user": user,
                            "movie": movie,
                            "date": date,
                            "rating": rating
                        }
                    valid_reviews.append(dict_of_review)
                    if movie not in movies:
                        movies.append(movie)
                    if user not in users:
                        users.append(user)
                    if date not in dates:
                        dates.append(date)
                else:
                    invalid.append((review, error))
            else:
                continue
        for item in movies:
            sum_of_ratings = 0
            count = 0
            for i in valid_reviews:
                if ("movie", item) in i.items():
                    sum_of_ratings += i['rating']
                    count += 1
                else:
                    continue
            average_rating_of_movies.append(
                f"{item}: {round((sum_of_ratings/count), 1)}")
        for item in users:
            review_count = 0
            for i in valid_reviews:
                if ("user", item) in i.items():
                    review_count += 1
            ratings_of_users.append(f"{item}: {review_count} reviews")
        positive = ["great", "amazing", "fantastic", "awesome",
                    "brilliant", "masterpiece", "beautiful", "excellent", "wonderful"]
        negative = ["bad", "boring", "terrible", "disappointing",
                    "confusing", "awful", "dull", "poor"]
        for m in movies:
            positive_count = 0
            negative_count = 0
            for item in valid_reviews:
                if item['movie'] == m:
                    positive_words = 0
                    negative_words = 0
                    if "comment" in item:
                        content_word = item["comment"].split()
                        for i in content_word:
                            if i in positive:
                                positive_words += 1
                            elif i in negative:
                                negative_words += 1
                    if positive_words > negative_words:
                        positive_count += 1
                    elif negative_words > positive_words:
                        negative_count += 1
                    elif positive_words == negative_words:
                        continue
            if positive_count > negative_count:
                sentiment_calculation.append(
                    f"{m}: +{positive_count-negative_count}")
            elif positive_count == negative_count:
                sentiment_calculation.append(f"{m}: 0")
            else:
                sentiment_calculation.append(
                    f"{m}: {positive_count-negative_count}")
        for d in dates:
            count_of_date = ""
            for item in valid_reviews:
                if ("date", d) in item.items():
                    count_of_date += "*"
                else:
                    continue
            dates_with_review_number.append(
                (d, f"{count_of_date} {len(count_of_date)}"))
    with open('../summary.txt', 'a+') as f:
        f.write("==== MOVIE RATING SUMMARY ====\n")
        for i in average_rating_of_movies:
            f.write(f"{i}\n")
        f.write("\n==== MOST ACTIVE USERS ====\n")
        for i in ratings_of_users:
            f.write(f"{i}\n")
        f.write("\n==== REVIEWS PER DAY ====")
        for i in dates_with_review_number:
            f.write(f"{i}\n")
        f.write("\n==== SENTIMENT ANALYSIS ====")
        for i in sentiment_calculation:
            f.write(f"{i}\n")
    return f"Processed {len(valid_reviews) + len(invalid)}:\n    {len(valid_reviews)} valid entries\n    {len(invalid)} malformed entries skipped"


print(process_file("trial_input.txt"))
