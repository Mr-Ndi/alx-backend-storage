-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_corrections INT;
    DECLARE average FLOAT;
    
    -- Calculate the total score and total corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_corrections
    FROM corrections
    WHERE user_id = ComputeAverageScoreForUser.user_id;
    
    -- Calculate the average score
    SET average = total_score / total_corrections;
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = average
    WHERE id = ComputeAverageScoreForUser.user_id;
END$$
DELIMITER ;