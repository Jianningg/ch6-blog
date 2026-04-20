from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_post_body_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="body",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
