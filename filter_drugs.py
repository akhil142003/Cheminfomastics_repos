""" Molecular Weight filter for Chemical compunds
-------------------------------------------------
--------------------
Reads PubChem CSV data and separates compounds based on molecular weight threshold as given 
by the user
"""

import csv
import sys

def molecular_weight_filter(filename, threshold=300):
    """ Filters compounds from PubChem CSV by molecular weight.
        
        Args:
            Filename : Path to PubChem CSV file
            threshold : Molecular weight cutoff(default : 300)
        Returns:
            Tuple of two dictionaries : (light_compounds, heavy_compounds)
    """
    light_compounds = {}
    heavy_compounds = {}

    try:

        with open(filename, 'r') as f:
            reader = csv.reader(f) #gives a list of data
            header = next(reader)

            for data in reader:
                weight = float(data[14])
                drug_name = data[1]

                if weight < threshold:
                    light_compounds[drug_name] = weight

                else:
                    heavy_compounds[drug_name] = weight

    except FileNotFoundError:
        print(f"Error : File  {filename} not found!")
        return None, None

    except ValueError:
        print("Error : Invalid data in file")
        return None, None

    except IndexError:
        print("Error : file format doen't match expected PubChem CSV structure")
        print("Make Sure Column 14 contains molecular weight")
        return None, None

    return light_compounds, heavy_compounds
   
    
def save_results(light_compounds, heavy_compounds,threshold=300):
    """ Save filtered results to next files."""

    #Save light componds
    
    with open('light_drugs.txt','w') as file:
        file.write(f'Drugs having M.W. < {threshold} are:\n')
        file.write('-' * 40 + '\n')
        for drug_name, weight in light_compounds.items():
            file.write(f'{drug_name} : {weight:.2f} g/mol\n')

    #Save heavy compounds

    with open('heavy_drugs.txt','w') as file2:
        file2.write(f'Drugs having M.W. > {threshold} are:\n')
        file2.write('-' * 40 + '\n')
        for drug_name, weight in heavy_compounds.items():
            file2.write(f'{drug_name} : {weight:.2f} g/mol\n')

def sorted_compounds(light_compounds, heavy_compounds):
    """ Gives the sorted list of compunds based on Molecular Weight 
    ---------------------------------------------------------------
    ----------
    """
    #sorted by weight
    all_drugs = {**light_compounds, **heavy_compounds} # merges both dictionary
    sort_drugs = sorted(all_drugs.items(), key=lambda x: x[1])
    with open('sorted_drugs.txt','w') as fi:
        fi.write('Sorted Compounds list\n')
        fi.write('-' * 40 + '\n')
        for name, weight in sort_drugs:
            fi.write(f'{name} : {weight:.2f} g/mol\n')



def heaviest_lightest_compounds(light_compounds, heavy_compounds):
    """ Gives Heaviest and lightest compound from composition 
    ---------------------------------------------------------
    ----------
    """
    all_drugs = {**light_compounds, **heavy_compounds}
    heaviest_compound = max(all_drugs, key=all_drugs.get)
    lightest_compound = min(all_drugs, key=all_drugs.get)
    print(f'Heaviest : {heaviest_compound} : ({all_drugs[heaviest_compound]}) g/mol')
    print(f'Lightest : {lightest_compound} : ({all_drugs[lightest_compound]})g/mol')


def average_of_weight(light_compounds, heavy_compounds):
    """ Calculates Average of all the weights
    -----------------------------------------
    ------
    """
# Average weight
    all_drugs = {**light_compounds, **heavy_compounds}
    total = sum(all_drugs.values())
    Average = total/len(all_drugs)
    print(f'Average molecular weight : {Average:.2f} g/mol')


def main():
    #get filename from command line or prompt
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the CSV filename with path : ")

    filename = filename.strip().strip('"').strip("'")

    threshold =300

    print(f"Processing : {filename}....")
    light, heavy = molecular_weight_filter(filename,threshold)

    if light is None or heavy is None:
        return

    save_results(light, heavy, threshold)

    print(f"Complete!")
    print(f"Light Compounds (<{threshold} g/mol): {len(light)}")
    print(f"Heavy Compounds (>={threshold} g/mol): {len(heavy)}")
    print("\nCheck 'light_drugs.txt' and 'heavy_drugs.txt' for results.")
    print("Check 'sorted_drugs.txt' for sorted list of compounds.")

    print("="*50 + '\n')
    sorted_compounds(light, heavy)
    heaviest_lightest_compounds(light, heavy)
    average_of_weight(light, heavy)
    print("-----------Analysis complete----------")

if __name__ == "__main__":
    main()





    



    

    


    

    

    

    

    
