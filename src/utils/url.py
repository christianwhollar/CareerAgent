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

def get_monster_url(q='', where_city='', where_state='', page=1, et_tuple_index=0, recency_tuple_index=0):
    base_url = 'https://www.monster.com/jobs/search?'

    # Set of all valid U.S. state abbreviations
    valid_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
                    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}
    
    # Validate state abbreviation
    if where_state not in valid_states:
        raise ValueError(f"Invalid state: {where_state}. Must be a valid U.S. state abbreviation.")
    
    # Validate index ranges for employment type and recency
    if not (0 <= et_tuple_index <= 4):
        raise ValueError("et_tuple_index must be between 0 and 4.")
    if not (0 <= recency_tuple_index <= 5):
        raise ValueError("recency_tuple_index must be between 0 and 5.")

    # Process inputs for URL
    q = q.replace(" ", "+")
    where = f'{where_city.replace(" ", "+")}%2C+{where_state}'

    # Tuples for employment type and recency options
    et_tuple = tuple(item.upper().replace(' ', '_') for item in ('Full Time', 'Part Time', 'Contract', 'Intern', 'Temp'))
    recency_tuple = tuple(item.replace(' ', '+') for item in ('', 'today', 'last 2 days', 'last week', 'last 2 weeks', 'last month'))

    # Select options based on provided indexes
    et = et_tuple[et_tuple_index]
    recency = recency_tuple[recency_tuple_index]

    # Dictionary of URL parameters
    extension_dict = {
        'q': q,
        'where': where,
        'page': str(page),  # Ensure page is converted to string
        'et': et,
        'recency': recency
    }

    # Assemble final URL
    url = base_url + '&'.join(f"{key}={value}" for key, value in extension_dict.items() if value)

    return url

def get_careerbuilder_url(posted='1', radius_tuple_index=2, cb_apply='false', keywords='engineer', location_city='', location_state='', pay='60', emp_tuple_index=0, cb_veterans='false', cb_workhome_tuple_index=0):
    # Base URL for CareerBuilder job search
    base_url = 'https://www.careerbuilder.com/jobs?'

    # Set of all valid U.S. state abbreviations
    valid_states = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
                    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}

    # Validate state abbreviation
    if location_state not in valid_states:
        raise ValueError(f"Invalid state: {location_state}. Please provide a valid state abbreviation (e.g., NY, PA, NC).")

    # Validate index ranges
    if not (0 <= radius_tuple_index <= 3):
        raise ValueError("radius_tuple_index must be between 0 and 3.")
    
    if not (0 <= emp_tuple_index <= 5):
        raise ValueError("emp_tuple_index must be between 0 and 5.")
    
    if not (0 <= cb_workhome_tuple_index <= 3):
        raise ValueError("cb_workhome_tuple_index must be between 0 and 3.")

    # Radius options (miles)
    radius_tuple = ('5', '10', '30', '50')
    radius = radius_tuple[radius_tuple_index]

    # Format location
    location = f'{location_city.replace(" ", "+")}%2C+{location_state}'

    # Employment type options
    emp_tuple = ('jtft%2Cjtfp', 'jtpt%2Cjtfp', 'jtct%2Cjtc2%2Cjtcc', 'jtch', 'jtse%2Cjttf%2Cjttp', 'jtfl')
    emp = emp_tuple[emp_tuple_index]

    # Work-from-home options
    cb_workhome_tuple = ('all', 'onsite', 'remote', 'hybrid')
    cb_workhome = cb_workhome_tuple[cb_workhome_tuple_index]

    # Assemble dictionary of URL parameters
    extension_dict = {
        'posted': posted,
        'radius': radius,
        'cb_apply': cb_apply,
        'keywords': keywords.replace(" ", "+"),
        'location': location,
        'pay': pay,
        'emp': emp,
        'cb_veterans': cb_veterans,
        'cb_workhome': cb_workhome
    }

    # Construct the final URL
    url = base_url + '&'.join(f"{key}={value}" for key, value in extension_dict.items() if value)

    return url