def get_ziprecruiter_url(search_value='', location_city='', location_state='', company='', refine_by_location_index=0, radius='', days='', refine_by_salary='', refine_by_employment_index=0):
    base_url = 'https://www.ziprecruiter.com/jobs-search?form=jobs-landing&'
    
    # Set of all valid U.S. state abbreviations
    valid_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
                    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}
    
    # Validate state abbreviation
    if location_state not in valid_states:
        raise ValueError(f"Invalid state: {location_state}. Must be a valid state abbreviation.")
    
    # Validate index ranges for location and employment type
    if not (0 <= refine_by_location_index <= 2):
        raise ValueError("refine_by_location_index must be between 0 and 2.")
    if not (0 <= refine_by_employment_index <= 2):
        raise ValueError("refine_by_employment_index must be between 0 and 2.")

    # Process inputs for URL
    search_value = search_value.replace(" ", "+")
    location = f'{location_city.replace(" ", "+")}%2C+{location_state}'

    # Tuples for location and employment type options
    refine_by_location_type_tuple = ('', 'no_remote', 'only_remote')
    refine_by_employment_tuple = tuple('employment_type%3A' + item for item in ('all', 'full_time', 'work_from_home'))

    # Select options based on provided indexes
    refine_by_location_type = refine_by_location_type_tuple[refine_by_location_index]
    refine_by_employment = refine_by_employment_tuple[refine_by_employment_index]

    # Dictionary of URL parameters
    extension_dict = {
        'search': search_value,
        'location': location,
        'company': company,
        'refine_by_location_type': refine_by_location_type,
        'radius': radius,
        'days': days,
        'refine_by_salary': refine_by_salary,
        'refine_by_employment': refine_by_employment
    }

    # Assemble final URL
    url = base_url + '&'.join(f"{key}={value}" for key, value in extension_dict.items() if value)

    return url
