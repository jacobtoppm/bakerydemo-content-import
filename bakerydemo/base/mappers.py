from wagtail_content_import.mappers.streamfield import StreamFieldMapper
from wagtail_content_import.mappers.converters import RichTextConverter, ImageConverter, TableConverter, TextConverter, BaseConverter


class SimpleMapper(StreamFieldMapper):
    html = RichTextConverter('paragraph')
    image = ImageConverter('image')
    heading = TextConverter('heading')
    table = TableConverter('table')


class HeadingBlockConverter(BaseConverter):
    def __call__(self, element, **kwargs):
        return (self.block_name, {'heading_text': element['value'], 'size': 'h2'})

class ImageBlockConverter(BaseConverter):
    def __call__(self, element, **kwargs):
        file_name, content = ImageConverter.fetch_image(element['value'])
        image = ImageConverter.import_as_image_model(file_name, content, kwargs['user'])
        return (self.block_name, {'image': image})

class BaseBlockMapper(StreamFieldMapper):
    html = RichTextConverter('paragraph_block')
    image = ImageBlockConverter('image_block')
    heading = HeadingBlockConverter('heading_block')
    table = TableConverter('table_block')
