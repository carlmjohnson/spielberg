from django.db import models


class Redirect(models.Model):

    to_url = models.URLField(
        blank=False,
        null=False,
        max_length=200,
        verbose_name="To",
        help_text="URL to redirect to"
    )
    status_code = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        choices=[
            (301, "301 Moved Permanently"),
            (302, "302 Found"),
            (303, "303 See Other"),
            (307, "307 Temporary Redirect"),
            (308, "308 Permanent Redirect"),
        ],
        default=302,
        help_text="HTTP Status Code",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_active_start = models.DateTimeField(blank=True, null=True)
    date_active_end = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(
        blank=True,
        null=False,
        help_text="Notes on why this redirect exists",
    )

    class Meta:
        abstract = True


class SimpleRedirect(Redirect):

    from_url = models.URLField(
        blank=False,
        null=False,
        max_length=200,
        unique=True,
        db_index=True,
        verbose_name="From",
        help_text="URL to redirect away from"
    )

    class Meta:
        ordering = ['from_url']
        index_together = [
            ('from_url', 'date_active_start', 'date_active_end'),
        ]

