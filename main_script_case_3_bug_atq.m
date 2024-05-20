% main_script_case_3_bug_atq
%
% This script categorizes participants into age groups based on their ages.
% 
% INPUTS
% ---------
% participants_initials: A cell array containing participants' initials.
% participants_ages    : A numeric array containing participants' ages.
% 
% OUTPUTS
% ---------
% None
% 
% The script iterates through each participant's age and assigns them to one of 
% three age groups: 'young', 'adult', or 'old', based on predefined age group boundaries. 
% Finally, it displays each participant's age and corresponding age group.
% 
% NOTE: This script was specifically created for the "Introducing Debugging - Unveiling the Power of Code Inspection"
% workshop, to illustrate an example where debugging with breakpoints is
% useful in MATLAB. 
%
% -----------------------------------------------------------------------------------------
% Ana Teresa Queiroga, 2024
% PhD student @ Department of Clinical Medicine, Center for Music in the Brain
% Aarhus University, Denmark


% List of participant's initials
participants_initials = {'AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', ...
                         'UV', 'WX', 'YZ', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', ...
                         'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', ...
                         'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ', 'AAA', ...
                         'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', ...
                         'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', ...
                         'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ', 'AAAA', 'BBBB', ...
                         'CCCC', 'DDDD', 'EEEE', 'FFFF', 'GGGG', 'HHHH', 'IIII', 'JJJJ', ...
                         'KKKK', 'LLLL', 'MMMM', 'NNNN', 'OOOO', 'PPPP', 'QQQQ', 'RRRR', ...
                         'SSSS', 'TTTT', 'UUUU', 'VVVV', 'WWWW', 'XXXX', 'YYYY', 'ZZZZ', ...
                         'AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'EEEEE', 'FFFFF', 'GGGGG', ...
                         'HHHHH', 'IIIII', 'JJJJJ', 'KKKKK', 'LLLLL', 'MMMMM', 'NNNNN', ...
                         'OOOOO', 'PPPPP', 'QQQQQ', 'RRRRR', 'SSSSS', 'TTTTT', 'UUUUU', ...
                         'VVVVV', 'WWWWW', 'XXXXX', 'YYYYY', 'ZZZZZ'};

% List of participants' ages
% Values in a list
participants_ages = [56, 63, 33, 27, 38, 39, 45, 50, 25, 36, 68, 21, 76, 64, 49, 55, 34, 47, 78, 53, ...
               51, 34, 49, 58, 61, 44, 42, 80, 22, 73, 75, 68, 26, 35, 40, 61, 28, 63, 26, ...
               59, 50, 67, 63, 75, 74, 40, 62, 32, 21, 65, 50, 49, 75, 57, 57, 72, 69, 55, ...
               31, 34, 74, 21, 49, 30, 79, 63, 50, 48, 23, 61, 22, 24, 51, 25, 69, 69, 64, ...
               29, 60, 51, 79, 59, 68, 47, 46, 70, 25, 28, 30, 43, 70, 69, 23, 44, 52, 45, ...
               60, 58, 37, 46, 20, 80, 30, 26, 42, 32, 49, 40, 78, 76, 23, 45, 36, 45, 65, 77];


%Define age group boundaries
young_age = 18;
adult_age = 31;
old_age   = 65;

% Iterate through participant's initials to get their ages
for i = 1:numel(participants_initials)
    
    % Get the age corresponding to the participant
    age = participants_ages(i);
    
    % Determine the age group
    if age >= young_age && age <= adult_age
        age_group = 'young';

    elseif age > adult_age && age < old_age
        age_group = 'adult';

    else
        age_group = 'old';
    end
    
    % Display participant's age and age group
    disp(['Participant ', participants_initials{i}, ' is ', num2str(age), ' years old, belongs to the ', age_group, ' age group.']);
    disp(' ')
end
