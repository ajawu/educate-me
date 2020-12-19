from .models import Donations


def get_book_donations_event(event_id):
    """
    Get all the books donated for an event
    :param event_id:
    :return:
    """
    book_donations = Donations.objects.filter(event_id=event_id, donation_type='book', fulfilled=True)
    book_count = 0
    for donation in book_donations:
        book_count += donation.item_count

    return book_count
