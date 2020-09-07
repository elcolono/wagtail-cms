# Generated by Django 3.0.10 on 2020-09-07 19:27

from django.db import migrations, models
import django.db.models.deletion
import section.models.hero
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks
import wagtail_color_panel.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('test', wagtail.core.blocks.StructBlock([('section', wagtail.snippets.blocks.SnippetChooserBlock(section.models.hero.HeroSection))]))], blank=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'verbose_name': 'Section Page',
                'verbose_name_plural': 'Section Pages',
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_action_bg_color_type', models.CharField(blank=True, choices=[('primary', 'Primary Color'), ('secondary', 'Secondary Color'), ('custom', 'Custom Color')], default='primary', help_text='Choose color type.', max_length=50, null=True, verbose_name='Color Type')),
                ('button_action_bg_color', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose background color.', max_length=7, null=True, verbose_name='Color')),
                ('button_action_bg_color_hover', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose hover background color', max_length=7, null=True, verbose_name='Color (hover)')),
                ('button_action_text_color', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose text color.', max_length=7, null=True, verbose_name='Text color')),
                ('button_action_text_color_hover', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose text hover color.', max_length=7, null=True, verbose_name='Text color (hover)')),
                ('button_action_font_weight', models.CharField(choices=[('font-hairline', 'Hairline'), ('font-thin', 'Thin'), ('font-light', 'Light'), ('font-normal', 'Default'), ('font-hairline', 'Hailine'), ('font-medium', 'Medium'), ('font-semibold', 'Semibold'), ('font-bold', 'Bold'), ('font-extrabold', 'Extrabold'), ('font-black', 'Black')], default='font-normal', help_text='Choose font weight.', max_length=50, null=True, verbose_name='Font weight')),
                ('button_action_padding', models.CharField(blank=True, choices=[('px-1 py-1', 'Small'), ('px-4 py-4', 'Medium'), ('px-8 py-8', 'Large'), ('px-12 py-12', 'X-Large')], help_text='Choose button size.', max_length=50, null=True, verbose_name='Size')),
                ('button_action_border_radius', models.CharField(blank=True, choices=[('rounded-none', 'None'), ('rounded-sm', 'Small'), ('rounded-md', 'Medium'), ('rounded-lg', 'Large'), ('rounded-full', 'Full')], help_text='Choose button edges.', max_length=50, null=True, verbose_name='Edges')),
                ('section_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('section_background_type', models.CharField(blank=True, choices=[('transparent', 'Transparent'), ('solid', 'Solid Color'), ('gradient', 'Gradient Color'), ('image', 'Background Image')], default='trasparent', help_text='Transparent background will use the background-color "page settings".', max_length=100, null=True)),
                ('section_background_color', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose background color', max_length=7, null=True, verbose_name='Background color')),
                ('section_background_color_2', wagtail_color_panel.fields.ColorField(blank=True, help_text='Choose background color', max_length=7, null=True, verbose_name='Background color 2')),
                ('hero_subheading', models.CharField(blank=True, default='What business are you?', help_text='Leave field empty to hide.', max_length=100, verbose_name='Hero subtitle')),
                ('hero_heading', models.CharField(blank=True, default='We are heroes', max_length=100, null=True, verbose_name='Hero title')),
                ('hero_layout', models.CharField(blank=True, choices=[('simple_centered', 'Simple centered'), ('image_right', 'Image on right')], default='simple_centered', max_length=100, verbose_name='Layout')),
                ('hero_description', models.TextField(blank=True, default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.', help_text='Leave field empty to hide.', max_length=400, verbose_name='Hero description')),
                ('hero_first_button_text', models.CharField(blank=True, default='Subscribe', help_text='Leave field empty to hide.', max_length=100, verbose_name='Hero button text')),
                ('hero_second_button_text', models.CharField(blank=True, default='Subscribe', help_text='Leave field empty to hide.', max_length=100, verbose_name='Hero button text')),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
