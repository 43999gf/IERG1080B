''''
 IERG 1080B Introduction to Python for Engineering Applications

 I declare that the assignment here submitted is original
 except for source material explicitly acknowledged,
 and that the same or closely related material has not been
 previously submitted for another course.
 I also acknowledge that I am aware of University policy and
 regulations on honesty in academic work, and of the disciplinary
 guidelines and procedures applicable to breaches of such
 policy and regulations, as contained in the website.

 University Guideline on Academic Honesty:
   http://www.cuhk.edu.hk/policy/academichonesty/

 Student Name : Leung Chi Hei
 Student ID   : 1155212427
 Class/Section: IERG1080B
 Date         : 16/1/2026
'''


def freeze_and_count(records):
    unique_ordered = []
    freq = {}
    seen = set()

    for name, scores in records:
        # TODO: freeze scores list into a tuple
        scores_tuple = tuple(scores)

        # TODO: make a hashable frozen record
        frozen_record = (name, scores_tuple)

        # TODO: update frequency dictionary (hint: .get)
        freq[frozen_record] = freq.get(frozen_record, 0) + 1

        # TODO: order-preserving dedup
        if frozen_record not in seen:
            unique_ordered.append(frozen_record)
            seen.add(frozen_record)

    return unique_ordered, freq


if __name__ == "__main__":
    # Try Sample run #1 and Sample run #2 here
    records = [
        ("Arpit", [100, 90]),
        ("Will", []),
        ("Arpit", [100, 90]),
        ("Chase", [88]),
    ]
    unique_ordered, freq = freeze_and_count(records)
    print(unique_ordered)
    print(freq)