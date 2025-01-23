def get_year_word_form(company_age):
    if company_age % 10 == 1 and company_age % 100 != 11:
        return "год"
    elif company_age % 10 in [2, 3, 4] and not (company_age % 100 in [12, 13, 14]):
        return "года"
    elif 11 <= company_age % 100 <= 20:
        return "лет"
    else:
        return "лет"
