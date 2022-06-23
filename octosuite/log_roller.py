'''
logRoller
This class is where the main notification strings/messages are held,
and are being used in two different cases (they're beig used by logging to be written to log files, and being printed out to the screen).
'''
class logRoller:
    Ctrl = 'Session terminated with {}.'
    Error = 'An error occurred: {}'
    sessionOpened = 'Opened new session on {}:{}'
    sessionClosed = 'Session closed at {}.'
    deletedLog = 'Deleted log: {}'
    readingLog = 'Reading log: {}'
    viewingLogs = 'Viewing logs...'
    fileDownloading = 'Downloading ({})...'
    fileDownloaded = 'Downloaded. Saved to downloads/{}'
    fileNotFound = 'File ({}) not found.'
    infoNotFound = 'Information ({} - {} - {}) not found.'
    repoNotFound = 'Repository ({}) not found.'
    userNotFound = 'User (@{}) not found.'
    orgNotFound = 'Organization (@{}) not found.'
    repoOrUserNotFound = 'Repository or user not found ({} - @{}).'
    askLogCsv = 'Do you wish to log this output to a .csv file? (Y/n) '
    loggedToCsv = 'Output logged to {}'
    loggingSkipped = '.csv logging skipped.'
    limitInput = ' Limit {} output to how many? (1-100) '
