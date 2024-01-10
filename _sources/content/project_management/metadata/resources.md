# Resources

This group represents all the items that make up of each Project. A resource can be a single media element (video, image, audio) or a group of media elements that create a unique resource. For example, it could be a set of images as part of a digitized manuscript or a group of videos describing a festivity.

You can use this [Template](../../../_static/files/Template_resources.xlsx) to assist you in organizing resource data.

## Group Resources Metadata Terms

## Identification

### Unique Record Identifier

| Term name     | Unique Record Identifier  |
| ------------- | ------------------------- |
| <span style="font-weight:bold;">Definition</span>    | An alphanumeric identifier for the record created for the IF Repository. |
| <span style="font-weight:bold;">Entry</span>    | String-CV – Unique Project Identifier (Projects)  |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:identifier](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#identifier) |
| <span style="font-weight:bold;">Repeatable</span>    | No  |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span>  |
| <span style="font-weight:bold;">Guideline</span>    | The Project Managers of each project will receive a pre-assigned unique project identifier. Unique ID's derivered from that ID and adding 4 digit secuential ordinal numbers.  |
| <span style="font-weight:bold;">Example</span>    | UFC00800001 |

### Original Identifier

| Term name     | Original Identifier |
| ------------- | ------------------- |
| <span style="font-weight:bold;">Definition</span>    | Original/Local identifier for the record given by the local project team. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | No |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | International or local identifiers associated with the original material. |
| <span style="font-weight:bold;">Example</span>    | CO 1/25 (National Archives Reference), 309.6 P.97 (Dewey Classification Number), AGN COL CI Folder 75, Document 2 (ISADG classification), 2019SG07-0239 (Unique ID of a digital collection) |

### Member Of

| Term name     | Member Of |
| ------------- | --------- |
| <span style="font-weight:bold;">Definition</span>    | Shows the parent collection or object which this record related to/part of. |
| <span style="font-weight:bold;">Entry</span>    | String-CV (Projects) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:isPartOf](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#isPartOf) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of the project as it is on the "Projects" sheet |
| <span style="font-weight:bold;">Example</span>    | Vernacular Songs as Archives and Modes of Social Redress in Jamestown, Accra |

### Resource Title Preferred

| Term name     | Resource Title Preferred |
| ------------- | ------------------------ |
| <span style="font-weight:bold;">Definition</span>    | The name given to the resource by the Creator (depositor) in any language.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#title)  |
| <span style="font-weight:bold;">Repeatable</span>    | No  |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide a short title for the resource in any language. Do not use any punctuation. Only capitalize the first alphabet of the project title, acronyms and any personal and geographic names.  |
| <span style="font-weight:bold;">Example</span>    | Aso wiwo awon obinrin ile Yoruba  |

### Resource Title Alternative

| Term name     | Resource Title Alternative |
| ------------- | -------------------------- |
| <span style="font-weight:bold;">Definition</span>    | The name given to the resource by the Creator (depositor) in other language.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:alternative](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#alternative)  |
| <span style="font-weight:bold;">Repeatable</span>    | No  |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide a translation or modified version of the title attributed to the record. |
| <span style="font-weight:bold;">Example</span>    | Local-made cloth of a typical Ghanian lady  |

### Digital Representations

| Term name     | Digital Representations |
| ------------- | ----------------------- |
| <span style="font-weight:bold;">Definition</span>    | Name of the digital file or the folder of multiple files. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | No  |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of the digital file. Or if you have more than one file to represent, provide the path of the folder. |
| <span style="font-weight:bold;">Example</span>    | Example_photo.jpg, UFC00800001/images/folder1 |

### External Link_Website Name

| Term name     | External Link_Website Name |
| ------------- | -------------------------- |
| <span style="font-weight:bold;">Definition</span>    | Name of the website where this resource was published. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    |   |
| <span style="font-weight:bold;">Example</span>    |   |

### External Link_Website URL

| Term name     | External Link_Website URL |
| ------------- | ------------------------- |
| <span style="font-weight:bold;">Definition</span>    | URL of the website where this resource was published. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |  |
| <span style="font-weight:bold;">Repeatable</span>    | No |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    |   |
| <span style="font-weight:bold;">Example</span>    |   |

## Scope and Content

### Resource Description

| Term name     | Resource Description |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | A textual description of the content of the resource (knowledge profile = images; documents) in any language, including event and significance connected to the resource. Content descriptions in the case of visual resources  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:description](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#description) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide textual description of the resource in English limited to maximum of three concise sentences. Include important keywords related to the significance of the resource. Since the description field is a potentially rich source of indexable vocabulary, care should be taken to provide this element when possible.  |
| <span style="font-weight:bold;">Example</span>    | Ile alo ti awon omode eya Arika lo ni odun to ti pe  |

### Resource Description Alternative

| Term name     | Resource Description Alternative |
| ------------- | -------------------------------- |
| <span style="font-weight:bold;">Definition</span>    | A textual description of the content of the resource in other language, including event and significance connected to the resource. Content descriptions in the case of visual resources  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:description](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#description) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide textual description of the resource in other language limited to maximum of three concise sentences. Include important keywords related to the significance of the resource. Since the description field is a potentially rich source of indexable vocabulary, care should be taken to provide this element when possible.  |
| <span style="font-weight:bold;">Example</span>    | Story book used for play by Pandalong children to understand the direction of the moon and sun. Created between 1908 and 1910.  |

### Primary Language

| Term name     | Primary Language |
| ------------- | ---------------- |
| <span style="font-weight:bold;">Definition</span>    | The primary language spoken by the participant (if video or audio resource). The primary language written on the image or in the document.  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Language)](./cv/1-languages.md) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:language](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#language)  |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span> if |
| <span style="font-weight:bold;">Guideline</span>    | Select the primary language spoken in the audio or video file. Select the primary language written on the image or in the document.  |
| <span style="font-weight:bold;">Example</span>    | English;Yoruba;Arabic  |

### Other Language

| Term name     | Other Language |
| ------------- | -------------- |
| <span style="font-weight:bold;">Definition</span>    | The other language spoken by the participant (if video or audio resource). The other language written on the image or in the document.  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Language)](./cv/1-languages.md)  |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:language](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#language)  |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Select the other language spoken in the audio or video file. Select the other language written on the image or in the document.  |
| <span style="font-weight:bold;">Example</span>    | English;Yoruba;Arabic  |

### Themes

| Term name     | Themes  |
| ------------- | ------- |
| <span style="font-weight:bold;">Definition</span>    | Descriptive words that are most significant and unique to the resource  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Themes)](./cv/2-themes.md) |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide maximum of five most significant and unique words that can describe the content of the resource. Separate each word with comma  |
| <span style="font-weight:bold;">Example</span>    | Colonised;Forgotten;Inclusion;Post-conflict;Refugee |

### Keywords

| Term name     | Keywords  |
| ------------- | --------- |
| <span style="font-weight:bold;">Definition</span>    | Descriptive words that are most significant and unique to the resource  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:subject](http://purl.org/dc/elements/1.1/subject) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide maximum of five most significant and unique words that can describe the content of the resource. Separate each word with comma  |
| <span style="font-weight:bold;">Example</span>    | Migration;Conflict;Community  |

### Notes

| Term name     | Notes |
| ------------- | ----- |
| <span style="font-weight:bold;">Definition</span>    | Any information that you want to add about this data, if you can not find a metadata field according to your need. |
| <span style="font-weight:bold;">Entry</span>    | String (Free text) |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |  <span style="color: green;">Optional</span>     |
| <span style="font-weight:bold;">Guideline</span>    |   |
| <span style="font-weight:bold;">Example</span>    |   |

## Spatial Coverage

### Country

| Term name     | Country  |
| ------------- | -------- |
| <span style="font-weight:bold;">Definition</span>    | The name of the country connected to the resource, where the content of the resource took place.  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Countries)](./cv/3-countries.md) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:spatial](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#spatial) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of the country that is connected to the resource.  |
| <span style="font-weight:bold;">Example</span>    | Argentina, Ghana, South Africa  |

### Region

| Term name     | Region  |
| ------------- | ------- |
| <span style="font-weight:bold;">Definition</span>    | The name of the region or state connected to the resource, where the content of the resource took place.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:spatial](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#spatial) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of the region/state/province that is connected to the resource.  |
| <span style="font-weight:bold;">Example</span>    | Osun, Chaco, Cape coast  |

### City

| Term name     | City |
| ------------- | ---- |
| <span style="font-weight:bold;">Definition</span>    | Administrative, jurisdictional or settlement named historicaly or oficially as a city.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:spatial](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#spatial) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |  <span style="color: green;">Optional</span>     |
| <span style="font-weight:bold;">Guideline</span>    |   |
| <span style="font-weight:bold;">Example</span>    |   |

### Address

| Term name     | Address |
| ------------- | ------- |
| <span style="font-weight:bold;">Definition</span>    | The name of the place/street name/area connected to the resource, where the content of the resource took place.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:spatial](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#spatial) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of the place/street name/area that is connected to the resource.  |
| <span style="font-weight:bold;">Example</span>    | Gbongan, Kishi, Sidwell Street  |

### Coordinates

| Term name     | Coordinates |
| ------------- | ----------- |
| <span style="font-weight:bold;">Definition</span>    | Point or array of points that represents the coordinates of a place in space. |
| <span style="font-weight:bold;">Entry</span>    | List of Coordinate Pairs (Floats) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:coverage](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#coverage) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |  <span style="color: green;">Optional</span>     |
| <span style="font-weight:bold;">Guideline</span>    | IT should be written as [lang,lat] |
| <span style="font-weight:bold;">Example</span>    | [10.77555,106.701944]; [10.77555,106.701944;11.74205,106.50001]; [10.77555,106.701944;11.74205,106.50001;9.2568,110.45406]|

### Non-Geolocated Place

| Term name     | Non-Geolocated Place |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | This element captures the names of places that do not have specific geographical coordinates or are of imaginary or mythical nature. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:coverage](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#coverage) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |  <span style="color: green;">Optional</span>     |
| <span style="font-weight:bold;">Guideline</span>    | Provide the name of a place or space |
| <span style="font-weight:bold;">Example</span>    | Aztlán, Atlantis, Tattooine |

## Socio-cultural Context

### Cultural Group

| Term name     | Cultural Group |
| ------------- | -------------- |
| <span style="font-weight:bold;">Definition</span>    | The cultural or ethnic group connected to the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Provide the names of all the cultural or ethnic group/community connected to the resource. This could be more than one.  |
| <span style="font-weight:bold;">Example</span>    | Arabs;Assyrians;Balanta  |

### Cultural Context

| Term name     | Cultural Context |
| ------------- | ---------------- |
| <span style="font-weight:bold;">Definition</span>    | The cultural event or context associated with the resource.  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Cultural Context)](./cv/4-cultural_context.md) |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Describe the cultural context or event associated with the resource. This descriptor responds to ‘What was happening when the resource was produced?’, ‘What event or practice is the resource recording?’ A list of suggested events is provided but add additional, more specific values to the vocabulary.  |
| <span style="font-weight:bold;">Example</span>    | Dancing;Migration;Singing |

### Social Group Setting

| Term name     | Social Group Setting |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | The social group associated with or recorded by the resource.  |
| <span style="font-weight:bold;">Entry</span>    | [String-CV (Social Group)](./cv/5-social_groups.md) |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Describe the social group associated with the resource. This descriptor responds to ‘What is the description of the people recorded by the resources?’ A list of suggested social group is provided but add additional, more specific values to the vocabulary.  e.g. <https://simplicable.com/society/social-groups> |
| <span style="font-weight:bold;">Example</span>    | Classmates;Family;Committees |

## Technology

### Production Technique

| Term name     | Production Technique |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | The defined way adopted to produce the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Describe the technique used in producing the resource. This descriptor responds to ‘How was the resource produced?’ A list of relevant production technique is provided but additional techniques can be added.  |
| <span style="font-weight:bold;">Example</span>    | Photography;Report writing;Audio recording;Video recording |

### Equipment used

| Term name     | Equipment used  |
| ------------- | --------------- |
| <span style="font-weight:bold;">Definition</span>    | The equipment used directly for the production of the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | List all the equipment used for the production of the resource. Provide the general names of each equipment, separated with commas.  |
| <span style="font-weight:bold;">Example</span>    | Tripod stand;DSLR camera;Video recording |

## Dates

### Date of creation

| Term name     | Date of creation  |
| ------------- | ----------------- |
| <span style="font-weight:bold;">Definition</span>    | A point or period of time associated with the creation of the resource.  |
| <span style="font-weight:bold;">Entry</span>    | Integer  |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:created](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#created) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Enter the date the resource was created. Recommended practice is to express date using the format YYYY-MM-DD [ISO 8601-1]. If the full date is unknown, month and year (YYYY-MM) or just year (YYYY) may be used.  |
| <span style="font-weight:bold;">Example</span>    | 2022-01-04 or 2022-01 or 2022  |

### Date of digitisation

| Term name     | Date of digitisation |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | A point or period of time associated with the digitisation of the resource. E.g. scanning, photographing date. |
| <span style="font-weight:bold;">Entry</span>    | Integer  |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Enter the date the resource was created. Recommended practice is to express date using the format YYYY-MM-DD [ISO 8601-1]. If the full date is unknown, month and year (YYYY-MM) or just year (YYYY) may be used.  |
| <span style="font-weight:bold;">Example</span>    | 2022-01-04 or 2022-01 or 2022  |

### Date of publication

| Term name     | Date of publication |
| ------------- | ------------------- |
| <span style="font-weight:bold;">Definition</span>    | A point or period of time associated with the publication of the resource. |
| <span style="font-weight:bold;">Entry</span>    | Integer  |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Enter the date the resource was created. Recommended practice is to express date using the format YYYY-MM-DD [ISO 8601-1]. If the full date is unknown, month and year (YYYY-MM) or just year (YYYY) may be used.  |
| <span style="font-weight:bold;">Example</span>    | 2022-01-04 or 2022-01 or 2022  |

## Access and Sensitivity

### Rights Ownership

| Term name     | Rights Ownership  |
| ------------- | ----------------- |
| <span style="font-weight:bold;">Definition</span>    | Information about the individual/community/groups/organisation who owns the rights in and over the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-CV (Participants) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:rightsHolder](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#rightsHolder) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Select the participant or community that owns the rights in and over the resource from the participants vocabulary. You can add names of individual/community/organisation that are not on the list to the vocabulary list, then here.  |
| <span style="font-weight:bold;">Example</span>    | Name Surname;University of Ghana;Ilesa community |

### Rights

| Term name     | Rights  |
| ------------- | -------- |
| <span style="font-weight:bold;">Definition</span>    | Information about the shareability, distribution and adaptation of the resource by users.  |
| <span style="font-weight:bold;">Entry</span>    | String-CV (Rights) |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:rights](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#rights) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span>  |
| <span style="font-weight:bold;">Guideline</span>    | Select which license, public domain mark or right statement is applicable to the resource. If not sure, select a restricted approach so the resource can be opened in the future. |
| <span style="font-weight:bold;">Example</span>    | CC BY-NC; In Copy Right|

### Cultural Sensitivity

| Term name     | Cultural Sensitivity |
| ------------- | -------------------- |
| <span style="font-weight:bold;">Definition</span>    | This refers to the attributed standard that governs the content and knowledge of the resources and who can access the resource. |
| <span style="font-weight:bold;">Entry</span>    | String-CV (Cultural sensitivity) |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span> |
| <span style="font-weight:bold;">Guideline</span>    | Select the level of cultural sensitivity of the content and knowledge of the resource. Consider this carefully before making your selection. ---Highly sensitive – refers to resource that cannot be viewed, downloaded, print nor accessed. The resources in this category are confidential. The depositor, persons connected to the project and repository administrators may have access to the resource. Moderately sensitive – refers to resources that are to be viewed only, not to be downloaded and print. Retrievers interested in accessing the resource need to fill ‘Data Retrieval Form’ to justify the need for the resource. Data Retrieval Form to be assessed and approved by the Principal Investigator and co-PIs. Low sensitivity – refers to resources that are to be shared openly. Retrievers will be able to view, download, print and use  |
| <span style="font-weight:bold;">Example</span>    | Highly sensitive, Low sensitive, Moderately sensitive  |

### Access restriction

| Term name     | Access restriction |
| ------------- | ------------------ |
| <span style="font-weight:bold;">Definition</span>    | This refers to availability of the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-CV – Access Restrictions  |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | No |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span> if |
| <span style="font-weight:bold;">Guideline</span>    | Select the level of access that is appropriate to the resource. "Accessible to public" will make the resource open to see and download for any visitor to the repository; "Not accessible to public" will keep the resource in private; "Restricted public access" makes the resource accessible only to registered users. This conditions can be change after the resource is ingested in the repository.  |
| <span style="font-weight:bold;">Example</span>    | "Accessible to public"  |

### Reasons for restriction

| Term name     | Reasons for restriction |
| ------------- | ----------------------- |
| <span style="font-weight:bold;">Definition</span>    | Justification for limiting access to the resources  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    |   |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: red;">Mandatory</span> if  |
| <span style="font-weight:bold;">Guideline</span>    | The field is <span style="color: red;">Mandatory</span> if the value for ‘Access restriction’ is Yes. Provide justifications for limiting the access to the resource and specify the consequences and potential impacts of making the resource accessible. Specify if access to the resource should ne restricted permanently or for a specific period of time.  |
| <span style="font-weight:bold;">Example</span>    | The image records various civil protests and disobedience is countries that are repressive. Making the image accessible could make the persons connected to the image targets. Therefore, access to the image should be permanently restricted.  |

## Intellectual Property

### Creator

| Term name     | Creator  |
| ------------- | -------- |
| <span style="font-weight:bold;">Definition</span>    | The individual that is primarily responsible for the production of the resource.  |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:creator](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#creator) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    | <span style="color: orangered;">Strongly Suggested</span> |
| <span style="font-weight:bold;">Guideline</span>    | Select the participant that is primarily responsible for the production of the resource. If many participants are involved, select the lead person for the production of the resource and list other as contributors.  |
| <span style="font-weight:bold;">Example</span>    | Name Surname;Name2 Surname2 |

### Contributors

| Term name     | Contributors  |
| ------------- | ------------- |
| <span style="font-weight:bold;">Definition</span>    | The individuals that supported the creator or contributed to the production of the resource. |
| <span style="font-weight:bold;">Entry</span>    | String-Free text |
| <span style="font-weight:bold;">DC equivalent</span>    | [dc:contributor](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#contributor) |
| <span style="font-weight:bold;">Repeatable</span>    | Yes |
| <span style="font-weight:bold;">Modality</span>    |<span style="color: green;">Optional</span>  |
| <span style="font-weight:bold;">Guideline</span>    | List all the individuals that contributed or supported the production of the resources. Separate each contributor with commas.  |
| <span style="font-weight:bold;">Example</span>    | Name Surname;Name2 Surname2  |
