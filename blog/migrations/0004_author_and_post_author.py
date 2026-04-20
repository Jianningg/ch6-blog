from django.db import migrations, models



def copy_user_to_author(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Author = apps.get_model("blog", "Author")
    User = apps.get_model("auth", "User")

    for post in Post.objects.all().iterator():
        user = User.objects.filter(pk=post.author_id).first()
        if user:
            first_name = user.first_name or user.username
            last_name = user.last_name or ""
            email = user.email or f"{user.username}@example.com"
        else:
            first_name = "Unknown"
            last_name = ""
            email = f"unknown-{post.pk}@example.com"

        author, _ = Author.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
            },
        )
        post.author_profile_id = author.id
        post.save(update_fields=["author_profile"])


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_add_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="author_profile",
            field=models.ForeignKey(
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="posts",
                to="blog.author",
            ),
        ),
        migrations.RunPython(copy_user_to_author, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="author_profile",
            new_name="author",
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                related_name="posts",
                to="blog.author",
            ),
        ),
    ]
